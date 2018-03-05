#!/usr/bin/env python3


def sync(drive_service, download_file, os, cloudnode, location):
    for node in cloudnode.children:
        node_location = location + '/' + node.title
        if node.mimeType == 'application/vnd.google-apps.folder':
            try:
                os.mkdir(node_location)
                sync(drive_service=drive_service, download_file=download_file,
                     os=os, cloudnode=node, location=node_location)
            except FileExistsError as e:
                print(e)
                pass
        else:
            if not os.path.isfile(node_location):
                download_file.DownloadFile(service=drive_service, file_id=node.id,
                                           create_file_destination=node_location)
