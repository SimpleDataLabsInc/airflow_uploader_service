"""Main module."""
from pathlib import Path
from typing import Union

from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()


@app.get("/hello")
def say_hello():
    return {"Hello": "World"}


@app.post('/upload')
async def upload_file(file: UploadFile = File(...), upload_folder: str = None):
    print(file,upload_folder)
    if upload_folder:
        upload_folder = Path(upload_folder)
        file_path = upload_folder / file.filename
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
