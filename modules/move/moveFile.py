def move_file(drive_service, file_id, previous_parent, new_parent):
    """
    Move the file to the new folder
    :param drive_service: service object for drive
    :param file_id: Id of file to move
    :param previous_parent: Id of previous parent of file
    :param new_parent: Id of new parent or folder
    :return: None
    """
    drive_service.files().update(fileId=file_id,
                                 addParents=new_parent,
                                 removeParents=previous_parent,
                                 fields='id, parents').execute()
