from apiclient import errors
from googleapiclient.http import MediaFileUpload


class UploadFile:
    @staticmethod
    def upload_file(service, title, parent_id, mime_type, filepath):
        """Insert new file.

        Args:
          service: Drive API service instance.
          title: Title of the file to insert, including the extension.
          parent_id: Parent folder's ID.
          mime_type: MIME type of the file to insert.
          filepath: Filepath of the file to insert.
        Returns:
          Inserted file metadata if successful, None otherwise.
        """
        media_body = MediaFileUpload(filepath, mimetype=mime_type, resumable=True)
        body = {
            'title': title,
            'mimeType': mime_type
        }
        # Set the parent folder.
        if parent_id:
            body['parents'] = [{'id': parent_id}]

        try:
            file = service.files().insert(
                body=body,
                media_body=media_body).execute()
            return file
        except errors.HttpError as e:
            print(e)
            return None
