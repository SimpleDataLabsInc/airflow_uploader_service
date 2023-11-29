from fastapi import APIRouter

from prophecy_pybridge.controller.hdfs_controller import HdfsController

router = APIRouter()
from fastapi import File, UploadFile


### HDFS FILE ROUTES
@router.post("/hdfs/upload_file")
def upload_hdfs_file(file: UploadFile = File(...), destination_dir: str = None):
    return HdfsController.upload_file(file, destination_dir)


@router.get("/hdfs/delete_file")
def delete_hdfs_file(file_path: str):
    return HdfsController.delete_file(file_path)


@router.get("/hdfs/delete_directory")
async def delete_hdfs_directory(directory_path: str):
    return HdfsController.delete_directory(directory_path)
