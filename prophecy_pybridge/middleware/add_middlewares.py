from fastapi import FastAPI, Request
from .basic_authentication import check_basic_authentication
from .process_time_header import add_process_time_header


def add_middlewares(app: FastAPI):
    @app.middleware("http")
    async def basic_authentication(request: Request, call_next):
        return await check_basic_authentication(request, call_next)

    @app.middleware("http")
    async def process_time_header(request: Request, call_next):
        return await add_process_time_header(request, call_next)
