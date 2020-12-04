from models.feedrequestargs import FeedRequestArgs

from utilities.conversion.to_json_converter import *

from urllib.request import urlopen
import requests
import json

allowedFeedTypes = ["xml", "csv"]

def get_and_parse_feed(feedRequstArgs: FeedRequestArgs):

    errorMsg = {"Status": "Error"}

    url = feedRequstArgs.url

    r = requests.get(url, allow_redirects=True)

    ext = r.headers['content-type'].split('/')[-1].split(";")[0] # get extension of file and character and splits again to only get extension

    if ext not in allowedFeedTypes:
        return {"Status": "Error: "+ ext +" is not a supported filetype"}
        
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
        

    if(toJson):
        return {
                    "status" : "Success",
                    "file" : {
                        "name": "feed",
                        "ext" : ext,
                        "content" : json.loads(toJson)
                    }
            }   
