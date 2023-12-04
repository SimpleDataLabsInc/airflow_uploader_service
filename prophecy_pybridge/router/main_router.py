from fastapi import APIRouter, Depends

from prophecy_pybridge.controller.file_controller import FileController

from fastapi import File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/hello")
def say_hello(name: str = "Prophecy") -> JSONResponse:
    """
    Sends a greeting message with the given name.

    :param name: (str) The name to be included in the greeting message. Default is "Prophecy".
    :return: (JSONResponse) A JSON response containing the greeting message.
    """
    return JSONResponse(content={"message": f"Hello {name}!"})
