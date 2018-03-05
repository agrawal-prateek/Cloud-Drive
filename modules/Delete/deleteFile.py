from apiclient import errors


class DeleteFile:
    @staticmethod
    def delete_file(service, file_id):
        """Permanently delete a file, skipping the trash.

        Args:
          service: Drive API service instance.
          file_id: ID of the file to delete.
        """
        try:
            return service.files().trash(fileId=file_id).execute()
        except errors.HttpError as e:
            print(e)
        return None
