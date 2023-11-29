"""Main module."""

from fastapi import FastAPI

from prophecy_pybridge.routers import routers

app = FastAPI(
    title="Prophecy PyBridge",
    description="Prophecy Bridge API",
    version="1.0.0",
)
API_PREFIX = "/api/v1"

# Include all the routers
for route in routers:
    app.include_router(router=route, prefix=API_PREFIX)
