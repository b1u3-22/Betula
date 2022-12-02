import json
import os
import shutil

FILE_PATH = f"{os.path.abspath('../../data')}/config.json"

def init_config():
    if (not os.path.exists(FILE_PATH)):
        shutil.copy("./config_default.json", FILE_PATH)

def get_config():
    with open(FILE_PATH, encoding="utf8") as config_file:
        return json.load(config_file)

def get_homepage_config():
    with open(FILE_PATH, encoding="utf8") as config_file:
        return json.load(config_file)["homePage"]

def get_dashboardpage_config():
    with open(FILE_PATH, encoding="utf8") as config_file:
        return json.load(config_file)["dashboardPage"]

def get_gallerypage_config():
    with open(FILE_PATH, encoding="utf8") as config_file:
        return json.load(config_file)["galleryPage"]

def update_config(new_config):
    with open(FILE_PATH, "w", encoding="utf8") as config_file:
        json.dump(new_config, config_file, indent=4)