#!/usr/bin/env python3

import json
import os
import re
import time

import httplib2
from apiclient import discovery
from oauth2client.file import Storage

from controllers import updateSettings
from modules.retrivechanges import retriveChangesOnCloud
from modules.token import currentCloudToken, currentDesktopToken


def item_in_savedcloudtree(saved_cloud_tree, item_id):
    for dictionary in saved_cloud_tree:
        if dictionary['id'] == item_id:
            return True
        if item_in_savedcloudtree(dictionary['children'], item_id):
            return True


while True:
    try:
        with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
            home_dir = home.read()
        if not os.path.isdir(home_dir + '/.clouddrive'):
            os.mkdir(home_dir + '/.clouddrive')
        if not os.path.isdir(home_dir + '/.clouddrive/changesOnCloud'):
            os.mkdir(home_dir + '/.clouddrive/changesOnCloud')

        credential_path = os.path.join('/etc/.credentials/.credentials.json')
        store = Storage(credential_path)

        credentials = store.get()
        http_auth = credentials.authorize(httplib2.Http(home_dir + '/.clouddrive/changesOnCloud'))

        service = discovery.build(serviceName='drive', version='v2', http=http_auth)
        desktopToken = currentDesktopToken.current_desktop_token()
        cloudToken = currentCloudToken.current_cloud_token(service)

        while True:
            print('desktoptoken = ', desktopToken, 'cloudtoken = ', cloudToken)

            # Check changes on cloud
            ids = retriveChangesOnCloud.retrive_changes(service, desktopToken)
            print(ids)

            # get updated cloud token
            cloudToken = currentCloudToken.current_cloud_token(service)

            # update desktop token
            try:
                print('n', 'desktopToken = ', desktopToken, 'cloudToken = ', cloudToken)
                listOfFiles = os.listdir(home_dir + '/.clouddrive/changesOnCloud')
                changesList = []
                for token in range(int(desktopToken), int(cloudToken)):
                    pattern = r'[a-z A-Z , & = 0-9 ]*pageToken=' + \
                              re.escape(str(token)) + '[a-z A-Z , & = 0-9 ]*'
                    for files in listOfFiles:
                        if re.findall(pattern, files):
                            changesList.append(home_dir + '/.clouddrive/changesOnCloud/' + files)
                            break
                print(changesList)

                # Starting synchronization...
                for fileLocation in changesList:
                    with open(fileLocation, 'r') as file:
                        data = file.read()

                    for i in range(len(data)):
                        if data[i] == '{':
                            data = data[i:]
                            break

                    data = json.loads(data)
                    for item in data['items']:

                        # check for parmanent deletion
                        if item['deleted']:
                            print('parmanent deleted')
                            continue

                        itemId = item['file']['id']

                        # check for trashed
                        if item['file']['labels']['trashed']:
                            # check if file exist on desktop
                            savedCloudTree = json.load(open(home_dir + '/.clouddrive/cloud/tree.json'))
                            if item_in_savedcloudtree(savedCloudTree['children'], itemId):
                                print(1)
                                pass
                # Finishing synchronization...

                updateSettings.update_settings(key='currentDesktopToken',
                                               value=str(cloudToken), data_type='int')
                desktopToken = cloudToken
                dirs = os.listdir(home_dir + '/.clouddrive/changesOnCloud')
                for i in dirs:
                    os.remove(home_dir + '/.clouddrive/changesOnCloud/' + i)
                print('synchronized')
            except PermissionError as e:
                print(e)
                exit(1)
    except httplib2.ServerNotFoundError as e:
        print(e)
        for timeRemaining in range(15):
            print('Trying reconnect in', 15 - timeRemaining, 'seconds')
            time.sleep(1)
        continue
    except Exception as e:
        print(e)
        exit(1)
