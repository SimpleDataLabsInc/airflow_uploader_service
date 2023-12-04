from fastapi import Request
import time


async def add_process_time_header(request: Request, call_next):
    """
    Add process time header to the response.

    :param request: The incoming request.
    :param call_next: The callable for processing the request and generating the response.
    :return: The response with X-Process-Time header added.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time) + " seconds"
    return response
