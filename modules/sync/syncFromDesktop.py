#!/usr/bin/env python3


def sync(drive_service, getDesktopTree, download_file, os, desktopnode, cloudnode, location):
    for cloudnode_child in cloudnode.children:
        child_location = location + '/' + cloudnode_child.title
        if cloudnode_child.mimeType == 'application/vnd.google-apps.folder':
            if not os.path.isdir(child_location):
                os.mkdir(child_location)
                new_node = getDesktopTree.create_node(name=cloudnode_child.title,
                                                      location=child_location, mime_type='inode/directory')
                getDesktopTree.append_child(parent=desktopnode, new_child=new_node)
            folder_object = None
            for node in desktopnode.children:
                if node.name == cloudnode_child.title:
                    folder_object = node
                    break
            sync(drive_service=drive_service, getDesktopTree=getDesktopTree,
                 download_file=download_file, os=os,
                 desktopnode=folder_object, cloudnode=cloudnode_child, location=child_location)
        else:
            if not os.path.isfile(child_location):
                download_file.DownloadFile(service=drive_service, file_id=cloudnode_child.id,
                                           create_file_destination=child_location)


def syncdrive(drive_service, getDesktopTree, download_file, googledrive, mydrive, location):
    print('synchronizing......')
    import os
    for my_drive_child in mydrive.children:
        nodelocation = location + '/' + my_drive_child.title
        if my_drive_child.mimeType == 'application/vnd.google-apps.folder':
            if not os.path.isdir(nodelocation):
                os.mkdir(nodelocation)
                new_node = getDesktopTree.create_node(name=my_drive_child.title, location=nodelocation,
                                                      mime_type='inode/directory')
                getDesktopTree.append_child(parent=googledrive, new_child=new_node)
                # googledrive = getDesktopTree.get_tree()
            google_drive_child = None
            for node in googledrive.children:
                if node.name == my_drive_child.title:
                    google_drive_child = node
                    break
            sync(drive_service=drive_service, getDesktopTree=getDesktopTree,
                 download_file=download_file, os=os,
                 desktopnode=google_drive_child, cloudnode=my_drive_child, location=nodelocation)

        else:
            if not os.path.isfile(nodelocation):
                download_file.DownloadFile(service=drive_service, file_id=my_drive_child.id,
                                           create_file_destination=nodelocation)
    print('synchronized')


syncdrive(drive_service=drive_service, getDesktopTree=getDesktopTree, download_file=downloadFile,
          googledrive=desktopTree, mydrive=cloudTree, location=location)
