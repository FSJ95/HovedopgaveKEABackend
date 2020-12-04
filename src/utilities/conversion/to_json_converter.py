import csv
import json
import xmltodict
import os


def xml_stream_to_json(xml_stream):
    """
        Takes an xml string and converts to json format in utf-8
    """

    xml_json = xmltodict.parse(xml_stream)
 
    jsonDump = json.dumps(xml_json, ensure_ascii=False)
    
    return jsonDump

def csv_file_to_json(csv_file_path):
    """
        Takes a csv file path, reads file and converts to json format
    """
    pass
