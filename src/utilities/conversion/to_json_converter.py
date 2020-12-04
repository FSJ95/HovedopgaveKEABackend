import csv
import json
import xmltodict
import os


def xml_stream_to_json(xml_stream):
    """
        Takes an xml string and converts to json format
    """
    #with open(xml_file_path, 'r') as xml_file:
        #xml_json = xmltodict.parse(xml_file.read())

    with open('./'+"test.xml", 'w', encoding="iso-8859-1") as f:
        f.write(xml_stream)      

    xml_json = xmltodict.parse(xml_stream)

    jsonDump = json.dumps(xml_json)  

    with open('./'+"test.json", 'w', encoding="iso-8859-1") as f:
        f.write(jsonDump)   
    
    return {"Status": "Sucess"}

def csv_file_to_json(csv_file_path):
    """
        Takes a csv file path, reads file and converts to json format
    """
    pass
