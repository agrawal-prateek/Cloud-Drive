#!/usr/bin/env python3

import os

# get location of home directory
home_dir = os.path.expanduser('~')

# Check .config directory if exist or not
if not os.path.isdir(home_dir + '/.config'):
    os.mkdir(home_dir + '/.config')

# Check .config/autostart directory if exist or not
if not os.path.isdir(home_dir + '/.config/autostart'):
    os.mkdir(home_dir + '/.config/autostart')

# Check if old startup entry exist or not
if os.path.isfile(home_dir + '/.config/autostart/cloud-drive.desktop'):
    os.system('sudo rm ' + home_dir + '/.config/autostart/cloud-drive.desktop')

os.system('cp components/startup/cloud-drive.desktop ' + home_dir + '/.config/autostart')

# add startup shortcut
if os.path.isdir('/usr/local/apps/cloud drive/startup'):
    os.system('sudo rm -r /usr/local/apps/cloud\ drive/startup')

# make startup directory in the installation directory
os.system('sudo mkdir /usr/local/apps/cloud\ drive/startup')

# add startup script
os.system('sudo cp components/startup/cloud-drive-startup.sh /usr/local/apps/cloud\ drive/startup')

