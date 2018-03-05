def retrive_changes(service, page_token=None):
    """Retrives the changes in Google Drive.
    Args:
        service: Drive API service instance.
        page_token: Last saved page token(Default None)
    Returns:
        tuple of id of files those have been changed
    """
    ids = ()
    while page_token is not None:
        response = service.changes().list(pageToken=page_token,
                                          spaces='drive').execute()
        for change in response.get('items'):
            # Process change
            ids += change.get('fileId'),
            page_token = response.get('nextPageToken')
    return ids
