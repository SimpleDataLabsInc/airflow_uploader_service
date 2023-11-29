from fastapi import APIRouter

from prophecy_pybridge.controller.hdfs_controller import HdfsController

router = APIRouter(prefix="/hdfs")
from fastapi import File, UploadFile


### HDFS FILE ROUTES
#Note - assumption is that we will be able to run hdfs commands on the node, as this service will be running on edge node
# if needed there is a way to authenticate and do this as well using python hdfs sdk

@router.post("/upload")
def upload_hdfs_file(file: UploadFile = File(...), destination_dir: str = None):
    return HdfsController.upload_file(file, destination_dir)


@router.get("/delete")
def delete_hdfs_file(file_path: str):
    return HdfsController.delete_file(file_path)


@router.get("/delete_directory")
def delete_hdfs_directory(directory_path: str):
    return HdfsController.delete_directory(directory_path)
