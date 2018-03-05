from __future__ import print_function

import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

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

CLIENT_SECRET_FILE = ".components/client_secret_159208223574-df125pk3gk61s6t2vp95p4i67ejcvkh3.apps.googleusercontent" \
                     ".com.json"
APPLICATION_NAME = 'Cloud Drive'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """

    credential_file = os.path.isfile('/etc/.credentials/.credentials.json')  # check if credentials exist

    if credential_file:
        os.system('sudo rm -r /etc/.credentials')

    if not credential_file:

        print('no old authentication found')
        home_dir = os.path.expanduser('~')  # get location of home directory

        try:
            if os.path.isdir(home_dir + '/.credentials'):
                os.system('sudo rm -r ' + home_dir + '/.credentials')
                print('successfully removed ' + home_dir + '/.credentials')
        except:
            print('There is some security issue with your system. Please contact to admin')
            return 1
        os.makedirs(home_dir + '/.credentials')  # make temporarily credentials directory in home
        store = Storage(home_dir + '/.credentials/.credentials.json')
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)

            flow.user_agent = APPLICATION_NAME
            if flags:
                tools.run_flow(flow, store, flags)
            else:
                tools.run(flow, store)
        current_credential_location = home_dir + '/.credentials'

        try:
            os.system('sudo mv ' + current_credential_location + ' /etc')
        except:
            print('There is some security issue with your system. Please contact to admin')
            return 1
        return 0


def main():
    try:
        if get_credentials() == 0:
            return 0
        else:
            return 1
    except:
        print('Authenticated unsuccessful! Some error occurred please try again')
        return 1


if __name__ == '__main__':
    if main() == 1:
        exit(1)
