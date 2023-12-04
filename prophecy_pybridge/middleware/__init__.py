from fastapi import FastAPI, Request
from . import basic_authentication
from . import process_time_header
from . add_middlewares import add_middlewares

# def add_middlewares(app: FastAPI):
#     @app.middleware("http")
#     async def basic_authentication(request: Request, call_next):
#         return await basic_authentication.check_basic_authentication(request, call_next)
#
#     @app.middleware("http")
#     async def process_time_header(request: Request, call_next):
#         return await process_time_header.add_process_time_header(request, call_next)
#
