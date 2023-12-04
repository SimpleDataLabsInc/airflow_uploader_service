from fastapi import Request
from fastapi.responses import JSONResponse
import base64

BASIC_AUTH_CREDS = {"username": "prophecy", "password": "Prophecy@123"}


def check_permission(method, api, auth):
    # The following paths are always allowed:
    if method == "GET" and api[1:] in ["docs", "openapi.json", "favicon.ico"]:
        return True
    # Parse auth header and check scheme, username and password
    scheme, data = (auth or " ").split(" ", 1)
    if scheme != "Basic":
        return False
    username, password = base64.b64decode(data).decode().split(":", 1)
    if (
        username == BASIC_AUTH_CREDS["username"]
        and password == BASIC_AUTH_CREDS["password"]
    ):
        return True


async def check_basic_authentication(request: Request, call_next):
    auth = request.headers.get("Authorization")
    if not check_permission(request.method, request.url.path, auth):
        return JSONResponse(None, 401, {"WWW-Authenticate": "Basic"})
    return await call_next(request)
