import base64

from fastapi import Request
from fastapi.responses import JSONResponse

BASIC_AUTH_CREDS = {"username": "prophecy", "password": "Prophecy@123"}


def check_permission(method, api, auth):
    """
    :param method: The HTTP method of the request (e.g. "GET", "POST", "PUT", etc.)
    :param api: The API endpoint being requested
    :param auth: The Authorization header value containing authentication information

    :return: True if the user has permission to access the given API endpoint using the specified HTTP method and authentication, False otherwise

    """
    # The following paths are always allowed:
    try:
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
    except ValueError:
        return False


async def check_basic_authentication(request: Request, call_next):
    """
    Check Basic Authentication

    :param request: The incoming request object.
    :param call_next: The callback function to call next middleware or route handler.
    :return: The response from the callback function.

    This method checks if the request has basic authentication headers and if the user has permission to access the requested resource. If the user does not have permission, it returns a 401 Unauthorized response with a WWW-Authenticate header. If the user has permission, it calls the next middleware or route handler.

    """
    auth = request.headers.get("Authorization")
    if not check_permission(request.method, request.url.path, auth):
        return JSONResponse({"message": "Access Denied"}
                            , 401, {"WWW-Authenticate": "Basic"}
                            )
    return await call_next(request)
