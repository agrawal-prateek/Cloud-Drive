
def current_cloud_token(service):
    """Get the the current state of the account.
    Args:
        service: Drive API service instance.
    Returns:
        int
    """
    response = service.changes().getStartPageToken().execute()
    return response.get('startPageToken')
