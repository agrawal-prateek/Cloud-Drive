#!/usr/bin/env python3

import os

home_dir = os.path.expanduser('~')

if not os.path.isdir(home_dir + '/.config/gtk-3.0'):
    os.mkdir(home_dir + '/.config/gtk-3.0')

if not os.path.isdir(home_dir + '/.config/gtk-2.0'):
    os.mkdir(home_dir + '/.config/gtk-2.0')

temp = 'file://' + home_dir + '/Google Drive'
bookmarkPath = ''

for i in temp:
    wordToAdd = i
    if i == " ":
        wordToAdd = '%20'
    bookmarkPath = bookmarkPath + wordToAdd

bookmarkPath = '\n' + bookmarkPath + ' Google Drive'

with open(home_dir + '/.config/gtk-3.0/bookmarks', "r") as myfile:
    temp = myfile.read()

    if bookmarkPath in temp:
        myfile.close()

    else:
        with open(home_dir + '/.config/gtk-3.0/bookmarks', "a") as myfile:
            myfile.write(bookmarkPath)
            myfile.close()

with open(home_dir + '/.config/gtk-2.0/bookmarks', "r") as myfile:
    temp = myfile.read()

    if bookmarkPath in temp:
        myfile.close()

    else:
        with open(home_dir + '/.config/gtk-2.0/bookmarks', "a") as myfile:
            myfile.write(bookmarkPath)
            myfile.close()
