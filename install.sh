#!/bin/bash

# create directory "Google drive" in home folder if it does not exist
if [[ ! -d /home/$USER/Google\ Drive ]]; then
    mkdir /home/$USER/Google\ Drive
fi

# Check if directory successfully created
if [ $? -eq 0 ]; then
    echo Successfully created directory /home/$USER/Google drive
else
    echo Could  not create directory /home/$USER/Google drive. Please contact to admin
fi

# Execute "main.py" with "python3" with root access
echo Waiting Authentication


if python3 main.py; then
    echo
else
    if python3 main.py; then
        echo
    else
        echo main.py failed
        exit 1
    fi
fi

python3 controllers/checkDependencies.py

echo Removing previous installation..........

# Remove previous installation if exist
sudo rm -rf /usr/local/bin/clouddrive
if [ $? -eq 0 ]; then
    echo removed /usr/local/bin/clouddrive
fi


# Copy configuration panel (clouddrive) to /usr/local/bin to access from terminal
sudo cp commands/clouddrive /usr/local/bin
if [ $? -eq 0 ]; then
    echo added command clouddrive
else
    echo Could not add command to /usr/local/bin......Application will not start
fi


#############################################
#### Now 'clouddrive' command will work #####
#############################################

# Create directory /usr/local/apps if does not exist
if [[ ! -d /usr/local/apps ]]; then
    sudo mkdir  /usr/local/apps
    echo Successfully created directory /usr/local/apps
fi

# Remove if installation directory cloud drive exist
if [[ -d /usr/local/apps/cloud\ drive ]]; then
    sudo rm -r /usr/local/apps/cloud\ drive
    echo Successfully removed directory /usr/local/apps/cloud drive
fi

# Create installation directory cloud Drive
sudo mkdir  /usr/local/apps/cloud\ drive
if [ $? -eq 0 ]; then
    echo Successfully created directory
else
    echo Could not create installation directory /usr/local/apps/cloud drive.........
    echo Application will not start
fi

# copy ui directory in /usr/local/apps/cloud drive
sudo cp -r ui /usr/local/apps/cloud\ drive

if [ $? -eq 0 ]; then
    echo Copied directory /usr/local/apps/cloud drive/ui
else
    echo Could not copy directory /usr/local/apps/cloud drive/ui
    exit 1
fi


# Copy components for clouddrive
sudo cp -r components/ui\ components /usr/local/apps/cloud\ drive

if [ $? -eq 0 ]; then
    echo Copied directory /usr/local/apps/cloud drive/ui components
else
    echo Could not copy directory /usr/local/apps/cloud drive/ui components
    exit 1
fi


# Copy cloud-drive-icon.png in /usr/share/icons
sudo cp components/shortcuts/cloud-drive-icon.png /usr/share/icons
if [ $? -eq 0 ]; then
    echo Successfully added icon Cloud Drive
else
    echo Could not add icon...........
    echo Application icon will not appear
fi

# Remove old shortcut if exist
sudo rm -rf /usr/share/applications/Cloud\ Drive.desktop

if [ $? -eq 0 ]; then
    echo Removed old shortcut Cloud Drive
fi

# Copy shortcut to launch
sudo cp components/shortcuts/Cloud\ Drive.desktop /usr/share/applications
sudo chmod +x /usr/share/applications/Cloud\ Drive.desktop

if [ $? -eq 0 ]; then
    echo Added a shortcut Cloud Drive......Now it can be accessed from start menu
else
    echo Could not add shortcut Cloud Drive to Start Menu.............
    echo You need to launch application via terminal by typing clouddrive
fi

#Create Desktop Entry
sudo rm -rf /home/$USER/Desktop/Cloud\ Drive.desktop
cp components/shortcuts/Cloud\ Drive.desktop /home/$USER/Desktop

# Create startup entry
python3 controllers/startupMaker.py
python3 controllers/bookmarkMaker.py

# Copy controllers in installation directory
sudo cp -r controllers /usr/local/apps/cloud\ drive

#copy modules
sudo cp -r modules /usr/local/apps/cloud\ drive

sudo cp sync.py /usr/local/apps/cloud\ drive
sudo cp __init__.py /usr/local/apps/cloud\ drive

python3 controllers/settingsInitializer.py
sudo mv HOME /usr/local/apps/cloud\ drive

#/usr/local/apps/cloud\ drive/startup/cloud-drive-startup.sh

echo
echo Installation Successful
echo LAUNCH APPLICATION BY STARTMENU OR TYPE "clouddrive" ON TERMINAL
echo For more info, Contact me at prateekagrawal89760@gmail.com
echo
