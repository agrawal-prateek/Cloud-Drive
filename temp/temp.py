#!/usr/bin/env python3
import json
import os

import httplib2
from apiclient import discovery
from oauth2client.file import Storage

from modules.Download import downloadFile


def build_tree(root, location):
    global TREE, TREE_FILE, files

    for fileItem in files:
        if fileItem['id'] == root['id']:
            if fileItem['mimeType'] == 'application/vnd.google-apps.folder':
                try:
                    os.mkdir(location)
                    fileItem['innodeNo'] = os.stat(location).st_ino
                    fileItem['modifiedOnDesktopDate'] = os.stat(location).st_mtime
                    fileItem['location'] = location
                    fileItem['children'] = []
                    for mainTreeItem in TREE:
                        if mainTreeItem['id'] == root['id']:
                            TREE.remove(mainTreeItem)
                            break
                    TREE.append(fileItem)
                    TREE_FILE.write(json.dumps(TREE))

                except FileExistsError as e:
                    print(e)
                    pass
            else:
                if not os.path.isfile(location):
                    downloadFile.DownloadFile(service=drive_service, file_id=root['id'],
                                              create_file_destination=location)
                    fileItem['innodeNo'] = os.stat(location).st_ino
                    fileItem['modifiedOnDesktopDate'] = os.stat(location).st_mtime
                    fileItem['location'] = location
                    fileItem['children'] = []
                    for mainTreeItem in TREE:
                        if mainTreeItem['id'] == root['id']:
                            TREE.remove(mainTreeItem)
                            break
                    TREE.append(fileItem)
                    TREE_FILE.write(json.dumps(TREE))
            break


if __name__ == '__main__':
    credential_path = os.path.join('/etc/.credentials/.credentials.json')
    store = Storage(credential_path)
    credentials = store.get()
    http_auth = credentials.authorize(httplib2.Http(".cache"))
    drive_service = discovery.build(serviceName='drive', version='v2', http=http_auth)

    with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
        HOME_DIR = home.read()

    TREE_LOCATION = '/home/prateek/.clouddrive/tree.json'
    TREE = {}
    TREE_FILE = None
    if os.path.isfile(TREE_LOCATION):
        TREE_FILE = open(TREE_LOCATION, 'r')
        previousContent = TREE_FILE.read()
        if previousContent:
            TREE = json.loads(previousContent)
        TREE_FILE.close()

    files = drive_service.files().list().execute()['items']
    if 'id' not in TREE.keys():
        root_details = drive_service.files().get(fileId="root").execute()
        TREE = root_details
        TREE['innodeNo'] = os.stat(HOME_DIR).st_ino
        TREE['modifiedOnDesktopDate'] = os.stat(HOME_DIR).st_mtime
        TREE['location'] = HOME_DIR + '/Google Drive'
        TREE['children'] = []
        files.append(TREE)

    with open(TREE_LOCATION, 'w+') as TREE_FILE:
        TREE_FILE.write(json.dumps(TREE))

    root_children = drive_service.children().list(folderId=TREE['id']).execute()
    root_children = root_children['items']

    for child in root_children:
        for fileItem in files:
            if fileItem['id'] == child['id']:
                if fileItem['mimeType'] == 'application/vnd.google-apps.folder':
                    try:
                        os.mkdir(TREE['location'] + '/' + fileItem['title'])
                        fileItem['innodeNo'] = os.stat(TREE['location'] + fileItem['title']).st_ino
                        fileItem['modifiedOnDesktopDate'] = os.stat(TREE['location'] + fileItem['title']).st_mtime
                        fileItem['location'] = TREE['location'] + '/' + fileItem['title']
                        fileItem['children'] = []
                        for mainTreeChild in TREE['children']:
                            if mainTreeChild['id'] == fileItem['id']:
                                TREE['children'].remove(mainTreeChild)
                                break
                        TREE['children'].append(fileItem)
                        with open(TREE_LOCATION, 'w+') as TREE_FILE:
                            TREE_FILE.write(json.dumps(TREE))
                        build_tree(TREE['children'], )

                    except FileExistsError as e:
                        print(e)
                        pass
                else:
                    if not os.path.isfile(TREE['location'] + '/' + fileItem['title']):
                        downloadFile.DownloadFile(service=drive_service, file_id=child['id'],
                                                  create_file_destination=TREE['location'] + '/' + fileItem['title'])
                        fileItem['innodeNo'] = os.stat(TREE['location'] + fileItem['title']).st_ino
                        fileItem['modifiedOnDesktopDate'] = os.stat(TREE['location'] + fileItem['title']).st_mtime
                        fileItem['location'] = TREE['location'] + '/' + fileItem['title']
                        fileItem['children'] = []
                        for mainTreeChild in TREE['children']:
                            if mainTreeChild['id'] == fileItem['id']:
                                TREE['children'].remove(mainTreeChild)
                                break
                        TREE['children'].append(fileItem)
                        with open(TREE_LOCATION, 'w+') as TREE_FILE:
                            TREE_FILE.write(json.dumps(TREE))
                break
