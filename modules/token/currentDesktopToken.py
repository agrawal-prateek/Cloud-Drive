import json


def current_desktop_token():
    """Function to get currentDesktopToken from settings.json
    Return:
        int
    """

    with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
        home_dir = home.read()
        home.close()

    json_file_loc = home_dir + '/.clouddrive/settings/settings.json'
    with open(json_file_loc, 'r') as json_settings_file:
        json_settings = json_settings_file.read()
        json_settings_file.close()
    current_token = json.loads(json_settings)['currentDesktopToken']

    return current_token
