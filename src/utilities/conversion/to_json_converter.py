import csv
import json
import xmltodict
import os
import io


def xml_stream_to_json(xml_stream):
    """
        Takes an xml string and converts to json format in utf-8
    """

    xml_json = xmltodict.parse(xml_stream)
 
    jsonDump = json.dumps(xml_json, ensure_ascii=False)
    
    return jsonDump

def csv_stream_to_json(csv_stream):
    """
        Takes an csv string and converts to json format in utf-8
    """

    csv_json = csv.DictReader(io.StringIO(csv_stream))
 
    jsonDump = json.dumps(list(csv_json), ensure_ascii=False)

    # with open('./'+"test.json", 'w', encoding='utf8') as f:
    #     f.write(jsonDump)
    
    return jsonDump
