#!/usr/bin/env python3

import json
import os
import time

import httplib2
from apiclient import discovery
from oauth2client.file import Storage

from controllers import updateSettings
from modules.Download import downloadFile
from modules.sync import initialSync
from modules.tree import getCloudTree
from modules.tree import getDesktopTree

credential_path = os.path.join('/etc/.credentials/.credentials.json')
store = Storage(credential_path)
credentials = store.get()
http_auth = credentials.authorize(httplib2.Http(".cache"))

drive_service = None
cloudTree = None
with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
    home_dir = home.read()

settings = json.load(open(home_dir + '/.clouddrive/settings/settings.json'))
desktopTreeFolderLocation = home_dir + '/.clouddrive/desktop'
desktopTreeFileLocation = home_dir + '/.clouddrive/desktop/tree.json'

while True:
    try:
        drive_service = discovery.build(serviceName='drive', version='v2', http=http_auth)
    except httplib2.ServerNotFoundError as e:
        print(e)
        for i in range(30):
            print('connection filed checking in', 30 - i, ' seconds...')
            time.sleep(1)
    else:
        break

if not settings['initialSync']:
    print('synchronizing...')

    while True:
        try:
            cloudTree = getCloudTree.get_tree(drive_service=drive_service)
        except httplib2.ServerNotFoundError as e:
            print(e)
            for i in range(30):
                print('connect  ion filed checking in', 30 - i, ' seconds...')
                time.sleep(1)
        else:
            if not cloudTree:
                continue
            break

    if not os.path.isdir(home_dir + '/.clouddrive'):
        os.mkdir(home_dir + '/.clouddrive')

    if not os.path.isdir(home_dir + '/.clouddrive/cloud'):
        os.mkdir(home_dir + '/.clouddrive/cloud')

    while True:
        if not getCloudTree.save_items_list(drive_service=drive_service,
                                            file_location=home_dir + '/.clouddrive/cloud/itemsList.json'):
            print("Couldn't fetch items list from cloud")
            print('retrying...')
        else:
            break

    initialSync.sync(drive_service=drive_service, download_file=downloadFile,
                     os=os, cloudnode=cloudTree,
                     location=settings['googleDriveLocation'])
    print('synchronized!')

    # build desktop tree
    desktopTree = getDesktopTree.get_tree()

    while True:
        try:
            if not os.path.isdir(desktopTreeFolderLocation):
                os.mkdir(desktopTreeFolderLocation)
            with open(desktopTreeFileLocation, 'w'):
                getDesktopTree.save_tree(root=desktopTree, file=desktopTreeFileLocation)

            getCloudTree.save_tree(root=cloudTree,
                                   file_location=home_dir + '/.clouddrive/cloud/tree.json')
            updateSettings.update_settings(key='initialSync', value='True', data_type='bool')
            break
        except Exception as e:
            print(e)
