from .basic_authentication import check_basic_authentication
from .process_time_header import add_process_time_header

middlewares = [check_basic_authentication, add_process_time_header]
