import json
import os

FILE_PATH = f"{os.path.abspath('../../data')}/config.json"


def get_config():
    with open(FILE_PATH, encoding="utf8") as config:
        return json.load(config)
