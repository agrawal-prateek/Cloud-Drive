from apiclient import errors


class CopyFile:
    @staticmethod
    def copy_file(service, origin_file_id, copy_title, new_parent_id):
        """Copy an existing file.

        Args:
          service: Drive API service instance.
          origin_file_id: ID of the origin file to copy.
          copy_title: Title of the copy.
          new_parent_id: Id of new parent folder

        Returns:
          The copied file if successful, None otherwise.
        """
        copied_file = {
            'title': copy_title,
            'parents': [{'id': new_parent_id}]
        }
        try:
            return service.files().copy(
                fileId=origin_file_id, body=copied_file).execute()
        except errors.HttpError as e:
            print(e)
        return None
