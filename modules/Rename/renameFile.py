from apiclient import errors


class RenameFile:
    @staticmethod
    def rename_file(service, file_id, new_title):
        """Rename a file.

        Args:
          service: Drive API service instance.
          file_id: ID of the file to rename.
          new_title: New title for the file.
        Returns:
          Updated file metadata if successful, None otherwise.
        """
        try:
            file = {'title': new_title}

            # Rename the file.
            updated_file = service.files().patch(
                fileId=file_id,
                body=file,
                fields='title').execute()

            return updated_file

        except errors.HttpError as e:
            print(e)
            return None
