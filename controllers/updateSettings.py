#!/usr/bin/env python3

import json


def update_settings(key, value, data_type):
    """
    update the settings in settings/settings.json

    :param data_type: data type of value
    :param key: property in settings.json file
    :param value: value of property
    """

    if data_type == 'bool':
        if value == 'True':
            value = True
        else:
            value = False
    if data_type == 'int':
        value = int(value)
    try:
        with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
            home_dir = home.read()
            home.close()

        with open(home_dir + '/.clouddrive/settings/settings.json', "r") as settingsFile:
            json_data = json.load(settingsFile)
            json_data[key] = value
            settingsFile.close()

        with open(home_dir + '/.clouddrive/settings/settings.json', "w") as settingsFile:
            settingsFile.write(json.dumps(json_data))
            settingsFile.close()

    except PermissionError as e:
        print(e)
