from utilities.conversion.to_json_converter import *
from models.link import Link

from fastapi import FastAPI
import re
from urllib.request import urlopen
import requests
import json

app = FastAPI()

allowedFeedTypes = ["xml, csv"]
allowedLinkTypes = ["csv", "json", "xml"]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/upload/feed")
def fetch_feed(link: Link):

    statusMessage = {"Status": "Error"}

    url = link.url

    r = requests.get(url, allow_redirects=True)

    ext = r.headers['content-type'].split('/')[-1].split(";")[0] # get extension of file and character and splits again to only get extension

    if ext not in allowedFeedTypes:
        return {"Status": "Error: Feed is not a supported filetype"}
        
    with urlopen(url) as x:
        data = x.read().decode('utf-8')

    if ext == 'csv':
        dump = csv_stream_to_json(data)

        if(dump):
            statusMessage = {"Status": "Success"} 

        return statusMessage        

    if ext == "xml":
        dump = xml_stream_to_json(data)

        if(dump):
            statusMessage = {"Status": "Success"}

        return statusMessage
        
    #TODO: Upload dump to S3 bucket

        # with open('./'+"test.json", 'w', encoding='utf8') as f:
        #     f.write(dump) 
    
    return statusMessage

@app.get("/upload/link/")
def fetch_file(link: Link):

    errorMsg = {"Status": "Error"}

    url = link.url

    if url.find('/'):
        name = url.rsplit('/', 1)[1]
        ext = name.rsplit('.', 1)[1]
        if ext not in allowedLinkTypes:
            return {"Status": "Error: "+ ext +" is not supported"}          

    with urlopen(url) as x:
        data = x.read().decode('utf-8')
        
    if ext == 'csv':
        toJson = csv_stream_to_json(data)
        if(not toJson):
            return errorMsg

    if ext == "xml":
        toJson = xml_stream_to_json(data)
        if(not toJson):
            return errorMsg      

    #TODO: Set all the requirements for how many objects, rotation osv

    # with open('/Users/olive/Desktop/'+nameAndType, 'w') as f:
    #     f.write(data)

    return {
                "status" : "Succes",
                "file" : {
                    "content" : json.loads(toJson),
                    "ext" : ext
                }
           }