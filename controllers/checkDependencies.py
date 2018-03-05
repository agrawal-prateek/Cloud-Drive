#!/usr/bin/env python3

# This file Checks all the dependencies packages for the application
# If any package doesn't exist, then It will install that package

import os


class CheckDependencies:
    @staticmethod
    def filemagic():  # Check package "filemagic"
        try:
            import magic
        except ImportError:
            # Installing Package "filemagic", which doesn't exist
            print("Installing package filemagic")
            os.system('sudo pip3 install filemagic --upgrade')


if __name__ == '__main__':
    CheckDependencies().filemagic()
