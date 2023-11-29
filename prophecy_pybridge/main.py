"""Main module."""

from fastapi import FastAPI

from prophecy_pybridge.routers import file, hdfs

app = FastAPI(
    title="Prophecy PyBridge",
    description="Prophecy Bridge API",
    version="1.0.0",
)

# Include the routers
app.include_router(file.router)
app.include_router(hdfs.router)
