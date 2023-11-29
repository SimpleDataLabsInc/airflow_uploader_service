from fastapi import APIRouter

from prophecy_pybridge.controller.file_controller import FileController

from fastapi import File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/file")


# LOCAL FILE ROUTES
@router.post("/upload")
def upload_file(
    file: UploadFile = File(...), destination_dir: str = None
) -> JSONResponse:
    return FileController.upload_file(file, destination_dir)


@router.get("/delete")
def delete_file(file_path: str) -> JSONResponse:
    return FileController.delete_file(file_path)


@router.get("/delete_directory")
def delete_directory(directory_path: str) -> JSONResponse:
    return FileController.delete_directory(directory_path)
