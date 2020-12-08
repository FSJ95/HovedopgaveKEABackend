import json
from utilities.conversion.to_json_converter import *

from controllers.filecontroller import *
from controllers.feedcontroller import *
from controllers.templatecontroller import *

from fastapi import FastAPI
from urllib.request import urlopen

app = FastAPI()

@app.get("/")
def index():

    return {"Message" : "This should show info about the API"}

@app.get("/templates")
def get_templates_request():

    return get_all_templates()

@app.get("/templates/{template_id}")
def get_template_request(template_id: int):

    return get_template(template_id)

@app.put("/templates/{template_id}")
def update_template_request(template_id: int, templateArgs: TemplateArgs):

    validation = validate_input(templateArgs)

    if(validation is not None):
        return validation   

    return update_template(template_id, templateArgs)

@app.delete("/templates/{template_id}")
def delete_template_request(template_id: int):

    return delete_template(template_id)   

@app.delete("/upload/{upload_id}")
def delete_upload(upload_id):
    
    return delete_upload_from_amazon(upload_id)

@app.get("/upload/feed")
def fetch_feed_request(feedRequstArgs: FeedRequestArgs):

    validation = validate_input(feedRequstArgs)

    if(validation is not None):
        return validation

    return get_and_parse_feed(feedRequstArgs)
    
@app.get("/upload/link/")
def fetch_file_request(fileRequestArgs: FileRequestArgs):

    validation = validate_input(fileRequestArgs)

    if(validation is not None):
        return validation   
    
    return get_and_parse_file(fileRequestArgs)

def validate_input(input):

    if(input == None):
        return {"status": "Error: input cannot be None"}

    #TODO: Add more validation

    return None