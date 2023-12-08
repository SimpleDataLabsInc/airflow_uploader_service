"""Unit test package for airflow_uploader_service."""
from base64 import b64encode

from airflow_uploader_service.middleware.basic_authentication import BASIC_AUTH_CREDS

test_credentials = f"{BASIC_AUTH_CREDS['username']}:{BASIC_AUTH_CREDS['password']}"
test_headers = {
    "Authorization": "Basic " + b64encode(test_credentials.encode()).decode()
}
