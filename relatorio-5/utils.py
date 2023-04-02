import json
import os
from bson import json_util  # pip install bson


def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))
    
    filePath = os.path.dirname(os.path.realpath(__file__))
    jsonFolder = os.path.join(filePath, "json")

    if not os.path.isdir(jsonFolder):
        os.makedirs(jsonFolder)

    with open(f"{jsonFolder}/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))