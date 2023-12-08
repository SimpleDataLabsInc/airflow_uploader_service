"""Main module."""

from fastapi import FastAPI

from airflow_uploader_service.middleware import middlewares
from airflow_uploader_service.router import routers

app = FastAPI(
    title="Prophecy PyBridge",
    description="Prophecy Bridge API",
    version="1.0.0",
)
API_PREFIX = "/api/v1"

# middlewares
for middleware in middlewares:
    app.middleware("http")(middleware)

# routers
for route in routers:
    app.include_router(router=route, prefix=API_PREFIX)
