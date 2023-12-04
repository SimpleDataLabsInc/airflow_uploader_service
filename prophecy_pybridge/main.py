"""Main module."""

from fastapi import FastAPI, Request

from prophecy_pybridge.middleware import add_middlewares
from prophecy_pybridge.routers import routers

API_VERSION = '1.0.0-dev0'

app = FastAPI(
    title="Prophecy PyBridge",
    description="Prophecy Bridge API",
    version=API_VERSION,
)
API_PREFIX = "/api/v1"

# Add all middlewares
add_middlewares(app)

# Include all the routers
for route in routers:
    app.include_router(router=route, prefix=API_PREFIX)
