from models.feedrequestargs import FeedRequestArgs

from controllers.bucketcontroller import *

from utilities.conversion.to_json_converter import *

from urllib.request import urlopen

import requests

allowedFeedTypes = ["xml", "csv", "rss+xml", "xhtml+xml"]

def get_and_parse_feed(feedRequstArgs: FeedRequestArgs):

    errorMsg = {"Status": "Error"}

    url = feedRequstArgs.url

    r = requests.get(url, allow_redirects=True)

    ext = r.headers['content-type'].split('/')[-1].split(";")[0] # get extension of file and character and splits again to only get extension

    if ext not in allowedFeedTypes:
        return {"Status": "Error: "+ ext +" is not a supported filetype"}
        
    with urlopen(url) as x:
        data = x.read().decode('utf-8')

    toJson = None

    if ext == 'csv':
        toJson = csv_stream_to_json(data)

        if not toJson:
            return errorMsg        

    if ext == "xml":
        toJson = xml_stream_to_json(data)

        if not toJson:            
            return errorMsg     

    if ext == "rss+xml":
        toJson = xml_stream_to_json(data)

        if not toJson:            
            return errorMsg     
    
    if ext == "xhtml+xml":
        toJson = xml_stream_to_json(data)

        if not toJson:            
            return errorMsg     

    #TODO: Update updateInterval and amountOfObjects in database¨

    #TODO: Refactor if statements to switch statement

    tempJson = json.loads(toJson)
    newJson = json.dumps(tempJson["rss"]["channel"]["item"])

    return upload_feed_and_return(newJson, ext)

def upload_feed_and_return(jsonData, ext):

    if upload_file(jsonData):
        return {
                    "status" : "Success",
                    "file" : {
                        "name": "feed",
                        "ext" : ext,
                        "content" : json.loads(jsonData)
                    }
                }      
    
    else:
        return {"status:" : "Error: Error in s3 upload"}
