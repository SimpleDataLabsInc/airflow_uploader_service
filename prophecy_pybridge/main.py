"""Main module."""

from fastapi import FastAPI, File, UploadFile
from prophecy_pybridge.controller.file_controller import FileController

app = FastAPI()


@app.get("/hello")
def say_hello():
    return {"Hello": "World"}


@app.get("/spec")
def openapi_spec():
    return {"info": app.openapi_schema}


@app.post("/upload")
def upload_file(file: UploadFile = File(...), destination_dir: str = None):
    FileController.upload_file(file, destination_dir)


@app.get("/delete")
def delete_file(file_path: str):
    FileController.delete_file(file_path)


@app.get("/deleteDir")
async def delete_directory(directory_path: str):
    FileController.delete_directory(directory_path)
