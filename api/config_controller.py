import json
import os

FILE_PATH = f"{os.path.abspath('../../data')}/config.json"


def get_config():
    with open(FILE_PATH, encoding="utf8") as config_file:
        return json.load(config_file)

def update_config(new_config):
    with open(FILE_PATH, "w", encoding="utf8") as config_file:
        json.dump(new_config, config_file, indent=4)