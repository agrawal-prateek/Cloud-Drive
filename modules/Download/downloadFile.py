from apiclient import errors
from apiclient import http


# ############################### Downloading ####################################

class DownloadFile:
    def __init__(self, service, file_id, create_file_destination):

        myfile = None

        try:
            myfile = open(create_file_destination, 'wb')
        except (PermissionError, IOError) as e:
            print(e)

        request = service.files().get_media(fileId=file_id)
        media_request = http.MediaIoBaseDownload(myfile, request)

        while True:
            try:
                download_progress, done = media_request.next_chunk()
            except errors:
                print('Couldn\'t download the file. An error occurred', errors)
                break
            if download_progress:
                print('Download Progress:', int(download_progress.progress() * 100))
            if done:
                print('Download Complete')
                break
