from models.filerequestargs import FileRequestArgs

from utilities.conversion.to_json_converter import *

from urllib.request import urlopen
import json

allowedLinkTypes = ["csv", "json", "xml"]

def get_and_parse_file(fileRequestArgs: FileRequestArgs):
    
    errorMsg = {"Status": "Error"}

    url = fileRequestArgs.url

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

    # with open('/Users/olive/Desktop/'+nameAndType, 'w') as f:
    #     f.write(data)

    return toJson
