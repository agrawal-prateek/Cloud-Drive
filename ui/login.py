#!/usr/bin/env python3


from __future__ import print_function

import os
import sys
import time

import httplib2
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

sys.path.append('/usr/local/apps/cloud drive')
from modules.getWebpage import getwebpage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

print('Logging in.....')

if os.path.isfile('/etc/.credentials/.credentials.json'):
    print('\nYou are already logged in. First logout then try again.\n')
    exit(0)

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.appdata",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.metadata",
    "https://www.googleapis.com/auth/drive.metadata.readonly",
    "https://www.googleapis.com/auth/drive.photos.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.scripts"
]


with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
    home_dir = home.read()
    home.close()

try:
    with open(home_dir + '/.clouddrivetemp.json', 'w+') as credentialFile:
        try:
            credentialString = getwebpage.get_page('http://cloud-drive-180821.appspot.com/credential')
            credentialFile.write(credentialString)
            credentialFile.close()
        except httplib2.ServerNotFoundError as e:
            print(e)
            exit('736572766572206e6f7420666f756e64')

    while True:

        try:
            CLIENT_SECRET_FILE = home_dir + '/.clouddrivetemp.json'
            APPLICATION_NAME = 'Cloud Drive'

            if not os.path.isdir('/etc/.credentials'):
                os.system('sudo mkdir /etc/.credentials')
            with open(home_dir + '/.templogin.json', 'w+') as temploginfile:
                temploginfile.close()
            store = Storage(home_dir + '/.templogin.json')
            credentials = store.get()
            if not credentials or credentials.invalid:
                flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
                flow.user_agent = APPLICATION_NAME
                if flags:
                    tools.run_flow(flow, store, flags)
                else:
                    tools.run(flow, store)
            os.system('sudo mv ' + home_dir + '/.templogin.json /etc/.credentials/.credentials.json')
            print('\nYou are now successfully logged in.\n')
            os.remove(home_dir + '/.clouddrivetemp.json')
            exit(0)
        except httplib2.ServerNotFoundError as e:
            print(e)
            print('Trying again in 10 seconds....')
            time.sleep(10)
except Exception as e:
    print(e)
    os.remove(home_dir + '/.clouddrivetemp.json')
    exit('66696c65206e6f742063726561746564')
