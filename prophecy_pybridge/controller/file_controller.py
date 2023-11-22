import os
import shutil
from pathlib import Path

from fastapi import UploadFile, File
from fastapi.responses import JSONResponse

class FileController(object):
    @staticmethod
    def upload_file(file: UploadFile = File(...), destination_dir: str = None):
        print(file, destination_dir)
        if destination_dir:
            destination_dir = Path(destination_dir)
            file_path = destination_dir / file.filename
            with file_path.open("wb") as buffer:
                try:
                    shutil.copyfileobj(file.file, buffer)
                    return JSONResponse(
                        content={
                            "filename": file.filename,
                            "file_path": str(file_path)
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
    def delete_file(file_path: str):
        try:
            os.remove(file_path)
            return JSONResponse(
                content={"message": f"File {file_path} deleted successfully."})
        except FileNotFoundError:
            return JSONResponse(status_code=500,
                                content={"error": f"File {file_path} not found."})
        except OSError as e:
            return JSONResponse(status_code=500,
                                content={"error": f"Error deleting file {file_path}: {e}"})

    @staticmethod
    def delete_directory(directory_path: str):
        try:
            shutil.rmtree(directory_path)
            return JSONResponse(
                content={"message": f"File {directory_path} deleted recursively successfully."})
        except OSError as e:
            print(f"Error deleting directory {directory_path}: {e}")
            return JSONResponse(status_code=500,
                                content={"error": f"Error deleting directory {directory_path}: {e}"})
