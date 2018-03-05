#!/usr/bin/env python3

import os

print('Logging you out')
os.system('sudo rm -r /etc/.credentials')
print('Yoy have successfully logged out.')

print('Do you want to keep your Google drive files on desktop(y/n)?:', end=' ')
res = input()

if res == 'y':
    exit(0)
else:
    print('Are you sure(y/n)?:', end=' ')
    res = input()
    if res == 'n':
        exit(0)
    else:
        with open('/usr/local/apps/cloud drive/HOME', 'r') as home:
            home_dir = home.read()
            home.close()

        print('removing files...')
        os.system('rm -r ' + home_dir + '/Google\ Drive')
        print('Successfully removed files')
        exit(0)


