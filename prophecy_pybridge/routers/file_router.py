from fastapi import APIRouter

from prophecy_pybridge.controller.file_controller import FileController

router = APIRouter()
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse


@router.get("/hello")
def say_hello(name: str = "Prophecy"):
    return JSONResponse(
        content={"message": f"Hello {name}!"})


### LOCAL FILE ROUTES
@router.post("/upload_file")
def upload_file(file: UploadFile = File(...), destination_dir: str = None):
    return FileController.upload_file(file, destination_dir)


@router.get("/delete_file")
def delete_file(file_path: str):
    return FileController.delete_file(file_path)


@router.get("/delete_directory")
async def delete_directory(directory_path: str):
    return FileController.delete_directory(directory_path)

