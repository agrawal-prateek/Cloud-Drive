import json
import os

import httplib2
from apiclient import discovery
from oauth2client.file import Storage

try:
    credential_path = os.path.join('/etc/.credentials/.credentials.json')
    store = Storage(credential_path)
    credentials = store.get()
    http_auth = credentials.authorize(httplib2.Http(".cache"))
    service = discovery.build('drive', 'v2', http_auth)

    response = service.changes().getStartPageToken().execute()
    currentDesktopToken = response.get('startPageToken')
    home_dir = os.path.expanduser('~')

    with open('HOME', 'w') as HOME:
        HOME.write(home_dir)

    try:
        os.mkdir(home_dir + '/.clouddrive')
        os.mkdir(home_dir + '/.clouddrive/settings')
    except FileExistsError:
        pass

    with open(home_dir + '/.clouddrive/settings/settings.json', "w") as settingsFile:
        d = dict()

        d['homeLocation'] = home_dir
        d['googleDriveLocation'] = home_dir + '/Google Drive'
        d['startup'] = True
        d["notifications"] = True
        d['bookmark'] = True
        d["currentDesktopToken"] = currentDesktopToken
        d['initialSync'] = False

        d = json.dumps(d)
        d = str(d)
        settingsFile.write(d)
        settingsFile.close()
        exit(0)

except httplib2.ServerNotFoundError as e:
    print(e)
    exit(1)
