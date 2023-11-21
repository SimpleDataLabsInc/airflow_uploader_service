import os
import shutil
from pathlib import Path

from fastapi import UploadFile, File


class FileController(object):
    @staticmethod
    def upload_file(file: UploadFile = File(...), destination_dir: str = None):
        print(file, destination_dir)
        if destination_dir:
            destination_dir = Path(destination_dir)
            file_path = destination_dir / file.filename
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            return {
                "STATUS": "SUCCESS",
                "filename": file.filename,
                "file_path": str(file_path)
            }
        else:
            return {
                "status": "ERROR",
                "cause": "Please provide a folder path"
            }

    @staticmethod
    def delete_file(file_path: str):
        try:
            os.remove(file_path)
            return {"message": f"File {file_path} deleted successfully."}
        except FileNotFoundError:
            return {"error": f"File {file_path} not found."}
        except OSError as e:
            return {"error": f"Error deleting file {file_path}: {e}"}

    @staticmethod
    def delete_directory(directory_path: str):
        try:
            shutil.rmtree(directory_path)
            print(f"Directory {directory_path} deleted successfully.")
        except OSError as e:
            print(f"Error deleting directory {directory_path}: {e}")

