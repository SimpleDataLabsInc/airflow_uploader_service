import os
import shutil
from pathlib import Path

from fastapi import UploadFile, File
from fastapi.responses import JSONResponse


class FileController(object):
    @staticmethod
    def upload_file(file: UploadFile = File(...), destination_dir: str = None) -> JSONResponse:
        """
        Uploads a file to a specified destination directory.

        :param file: The file to be uploaded. (type: UploadFile)
        :param destination_dir: The destination directory where the file should be uploaded. (type: str)
        :return: A JSONResponse object containing the filename and file path if the upload is successful. If there is an error, a JSONResponse object with an error message is returned. (type
        *: JSONResponse)
        """
        print(file, destination_dir)
        if destination_dir:
            destination_dir = Path(destination_dir)
            # create destination directory recursively, error if already file exists
            destination_dir.mkdir(parents=True, exist_ok=False)
            file_path = destination_dir / file.filename
            with file_path.open("wb") as buffer:
                try:
                    shutil.copyfileobj(file.file, buffer)
                    return JSONResponse(
                        content={
                            "filename": file.filename,
                            "file_path": str(destination_dir)
                        })
                except OSError as e:
                    print(f"Error uploading File: {file.filename}\n {e}")
                    return JSONResponse(status_code=500,
                                        content={"error": f"Error uploading file: {file.filename}\n {e}"})
            return JSONResponse(
                status_code=500,
                content={
                    "status": "ERROR",
                    "cause": "Error reading file buffer for upload"
                })
        else:
            return JSONResponse(
                status_code=500,
                content={
                    "status": "ERROR",
                    "cause": "Please provide a folder path"
                })

    @staticmethod
    def delete_file(file_path: str) -> JSONResponse:
        """
        :param file_path: The path of the file to be deleted.
        :return: JSONResponse object.

        This method is a static method that deletes the file specified by the given file_path. It uses the os.remove() function to remove the file. If the file is successfully deleted, it returns
        * a JSONResponse object with a success message. If the file is not found, a JSONResponse object with an error message indicating that the file was not found is returned. If there is
        * an OSError while deleting the file, a JSONResponse object with an error message and details of the OSError is returned.
        """
        try:
            os.remove(file_path)
            return JSONResponse(
                content={"message": f"File {file_path} deleted successfully."})
        except FileNotFoundError:
            return JSONResponse(status_code=500,
                                content={"error": f"File {file_path} not found."})
        except OSError as e:
            return JSONResponse(status_code=500,
                                content={"error": f"Error deleting file {file_path}",
                                         "details": f" {e}"
                                         })

    @staticmethod
    def delete_directory(directory_path: str) -> JSONResponse:
        """
        Delete a directory and its contents recursively.

        :param directory_path: The path of the directory to delete.
        :return: A JSONResponse object containing a success message or an error message.
        """
        try:
            shutil.rmtree(directory_path)
            return JSONResponse(
                content={"message": f"File {directory_path} deleted recursively successfully."})
        except OSError as e:
            print(f"Error deleting directory {directory_path}: {e}")
            return JSONResponse(status_code=500,
                                content={
                                    "error": f"Error deleting directory {directory_path}",
                                    "details": f" {e}"
                                })
