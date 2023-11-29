"""Main module."""

from fastapi import FastAPI, File, UploadFile
from prophecy_pybridge.controller.file_controller import FileController
from fastapi.responses import JSONResponse

from prophecy_pybridge.controller.hdfs_controller import HdfsController

app = FastAPI()


@app.get("/hello")
def say_hello(name: str = "Prophecy"):
    return JSONResponse(
        content={"message": f"Hello {name}!"})


### LOCAL FILE ROUTES
@app.post("/upload_file")
def upload_file(file: UploadFile = File(...), destination_dir: str = None):
    return FileController.upload_file(file, destination_dir)


@app.get("/delete_file")
def delete_file(file_path: str):
    return FileController.delete_file(file_path)


@app.get("/delete_directory")
async def delete_directory(directory_path: str):
    return FileController.delete_directory(directory_path)


### HDFS FILE ROUTES
@app.post("/hdfs/upload_file")
def upload_hdfs_file(file: UploadFile = File(...), destination_dir: str = None):
    return HdfsController.upload_file(file, destination_dir)


@app.get("/hdfs/delete_file")
def delete_hdfs_file(file_path: str):
    return HdfsController.delete_file(file_path)


@app.get("/hdfs/delete_directory")
async def delete_hdfs_directory(directory_path: str):
    return HdfsController.delete_directory(directory_path)
