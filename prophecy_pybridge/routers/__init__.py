from . import main_router
from . import file_router
from . import hdfs_router

routers = [main_router.router, file_router.router, hdfs_router.router]
