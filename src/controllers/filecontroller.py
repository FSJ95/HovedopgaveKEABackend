from models.filerequestargs import FileRequestArgs

from controllers.bucketcontroller import *

from utilities.conversion.to_json_converter import *

from urllib.request import urlopen

import uuid

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

    return upload_file_and_return(toJson, name, ext)

def upload_file_and_return(jsonData, name, ext):
    if(upload_file(jsonData)):
        return {
                    "status" : "Success",
                    "file" : {
                        "name": name,
                        "ext" : ext,
                        "content" : json.loads(jsonData)
                    }
                }      
    
    else:
        return {"status:" : "Error: Error in s3 upload"}