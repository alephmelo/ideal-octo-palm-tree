import json


def get_settings():
    with open('settings.json', 'r') as json_file:
        return json.load(json_file)
