from models.link import Link

from fastapi import FastAPI
import re
from urllib.request import urlopen

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/upload/link/")
def fetch_file(link: Link):

    url = link.url

    allowedTypes = ["csv", "json", "xml"]

    if url.find('/'):
        nameAndType = url.rsplit('/', 1)[1]
        print(nameAndType)
        onlyType = nameAndType.rsplit('.', 1)[1]
        print(onlyType)
        if onlyType not in allowedTypes:
            return {"Error": "Filetype not allowed"}          

    with urlopen(url) as x:
        data = x.read().decode('utf-8')
    
    #TODO: Do something with the fetched file 

    #TODO: Set all the requirements for how many objects, rotation osv

    # with open('/Users/olive/Desktop/'+nameAndType, 'w') as f:
    #     f.write(data)

    return {"Download": "Suceeded"}