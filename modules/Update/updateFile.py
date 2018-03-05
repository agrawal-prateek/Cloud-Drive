from apiclient import errors
from googleapiclient.http import MediaFileUpload


class UpdateFile:
    @staticmethod
    def update_file(service, file_id, new_title, new_mime_type,
                    new_filename, new_revision):
        """Update an existing file's metadata and content.

        Args:
          service: Drive API service instance.
          file_id: ID of the file to update.
          new_title: New title for the file.
          new_mime_type: New MIME type for the file.
          new_filename: Filename of the new content to upload.
          new_revision: Whether or not to create a new revision for this file.
        Returns:
          Updated file metadata if successful, None otherwise.
        """
        try:
            # First retrieve the file from the API.
            file = service.files().get(fileId=file_id).execute()

            # File's new metadata.
            file['title'] = new_title
            file['mimeType'] = new_mime_type

            # File's new content.
            media_body = MediaFileUpload(
                new_filename, mimetype=new_mime_type, resumable=True)

            # Send the request to the API.
            updated_file = service.files().update(
                fileId=file_id,
                body=file,
                newRevision=new_revision,
                media_body=media_body).execute()
            return updated_file
        except errors.HttpError as e:
            print(e)
            return None
