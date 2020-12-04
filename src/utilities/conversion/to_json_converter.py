import csv
import json
import xmltodict
import os
import io


def xml_stream_to_json(xml_stream):
    """
        Takes an xml string and converts to json format in utf-8
    """

    try:
        xml_json = xmltodict.parse(xml_stream)
        return json.dumps(xml_json, ensure_ascii=False)
    except Exception as identifier:
        return False

def csv_stream_to_json(csv_stream):
    """
        Takes a csv file path, reads file and converts to json format
    """
    try:
        csv_json = csv.DictReader(io.StringIO(csv_stream))
        return json.dumps(list(csv_json), ensure_ascii=False)
    except Exception as identifier:
        return False
