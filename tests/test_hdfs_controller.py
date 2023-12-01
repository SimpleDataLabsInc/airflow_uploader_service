#!/usr/bin/env python

"""Tests for `prophecy_pybridge` package."""
import os
import shutil

from fastapi.testclient import TestClient
from prophecy_pybridge.main import app, API_PREFIX

client = TestClient(app)
current_file_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "test.txt"
input_dir = current_file_dir + "/resources/input"
input_file_path = input_dir + f"/{file_name}"
output_hdfs_dir = "/pateash"


# only run in local can't run this on CI/CD
def test_upload_file():
    # first remove and then try this
    with open(input_file_path, "rb") as file:
        file_content = file.read()
        response = client.post(
            API_PREFIX + "/hdfs/upload",
            params={"destination_dir": output_hdfs_dir},
            files={"file": (file_name, file_content)},
        )
        data = response.json()
        print(data)

        assert response.status_code == 200
        assert  "test.txt" in data["message"]

#
# def test_delete_file():
#     # copy test file from input to output and then delete
#     # and check its existence
#     output_file_path = f"{output_dir}/delete_{file_name}"
#     shutil.copy(input_file_path, output_file_path)
#
#     assert os.path.exists(output_file_path)
#     response = client.get(
#         API_PREFIX + "/hdfs/delete",
#         params={"file_path": output_file_path},
#     )
#     assert not os.path.exists(output_file_path)
#
#     print(response)
#     assert response.status_code == 200
#     data = response.json()
#     assert "deleted successfully" in data["message"]
#     print(data)
#
#
# def test_delete_directory():
#     output_test_dir = f"{output_dir}/delete_dir"
#     shutil.copytree(input_dir, output_test_dir, dirs_exist_ok=True)
#     assert os.path.exists(output_test_dir)
#     response = client.get(
#         API_PREFIX + "/hdfs/delete_directory",
#         params={"directory_path": output_test_dir},
#     )
#     assert not os.path.exists(output_test_dir)
#     print(response)
#     assert response.status_code == 200
#     data = response.json()
#     assert "deleted recursively successfully" in data["message"]
#     print(data)
#
#
