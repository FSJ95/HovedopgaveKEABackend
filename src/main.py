from utilities.conversion.to_json_converter import *

from controllers.linkcontroller import *
from controllers.feedcontroller import *

from fastapi import FastAPI
from urllib.request import urlopen

app = FastAPI()

allowedFeedTypes = ["xml", "csv"]
allowedLinkTypes = ["csv", "json", "xml"]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/upload/feed")
def fetch_feed(feedRequstArgs: FeedRequestArgs):

    #TODO: Validation of input

    return get_and_parse_feed(feedRequstArgs)

    #TODO: Upload to S3 bucket
    
@app.get("/upload/link/")
def fetch_file(fileRequestArgs: FileRequestArgs):

    #TODO: Validation of input

    return get_and_parse_file(fileRequestArgs)

    #TODO: Upload to S3 bucket
