#!/usr/bin/env python3


import os


print('Logging you out')
os.system('sudo rm -r /etc/.credentials')
print('Successfully logged out.')

os.system('/usr/local/apps/cloud\ drive/ui/login.py')
