from utilities.conversion.to_json_converter import *

from controllers.linkcontroller import *
from controllers.feedcontroller import *

from fastapi import FastAPI
from urllib.request import urlopen
import sys

app = FastAPI()

allowedFeedTypes = ["xml", "csv"]
allowedLinkTypes = ["csv", "json", "xml"]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/upload/feed")
def fetch_feed(feedRequstArgs: FeedRequestArgs):

    validation = validate_input(feedRequstArgs)

    if(validation is not True):
        return validation

    return get_and_parse_feed(feedRequstArgs)

    #TODO: Upload to S3 bucket
    
@app.get("/upload/link/")
def fetch_file(fileRequestArgs: FileRequestArgs):

    validation = validate_input(fileRequestArgs)

    if(validation is not True):
        return validation   

    return get_and_parse_file(fileRequestArgs)

    #TODO: Upload to S3 bucket


def validate_input(input):

    if not(input.url):
        return {"Status": "Error: request must have a url"}

    if(input == None):
        return {"Status": "Error: input cannot be None"}

    if(sys.getsizeof(input, 0) == 0):
        return {"Status": "Error: input cannot be 0 bytes"}

    #TODO: Add more validation and fix current validation

    return True