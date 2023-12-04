"""Main module."""

from fastapi import FastAPI, Request

from prophecy_pybridge.middleware import add_middlewares
from prophecy_pybridge.routers import routers

app = FastAPI(
    title="Prophecy PyBridge",
    description="Prophecy Bridge API",
    version="1.0.0",
)
API_PREFIX = "/api/v1"

# Add all middlewares
add_middlewares(app)

# Include all the routers
for route in routers:
    app.include_router(router=route, prefix=API_PREFIX)
