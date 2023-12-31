#!/usr/bin/env python

"""Tests for `airflow_uploader_service` package."""
import os
import shutil

from fastapi.testclient import TestClient
from airflow_uploader_service.main import app, API_PREFIX
from . import test_headers

client = TestClient(app)
current_file_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "test.txt"
input_dir = current_file_dir + "/resources/input"
input_file_path = input_dir + f"/{file_name}"
output_dir = current_file_dir + "/resources/output"


def test_upload_file():
    output_file_path = f"{output_dir}/{file_name}"
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        print(f"Test File {output_file_path} removed successfully.")
    else:
        print(f"File {output_file_path} does not exist.")

    with open(input_file_path, "rb") as file:
        file_content = file.read()
        response = client.post(
            API_PREFIX + "/file/upload",
            params={"destination_dir": output_dir},
            files={"file": (file_name, file_content)},
            headers=test_headers,
        )
        # print(response)
        assert response.status_code == 200
        data = response.json()
        assert data["filename"] == "test.txt"
        assert output_dir in data["file_path"]


def test_delete_file():
    # copy test file from input to output and then delete
    # and check its existence
    output_file_path = f"{output_dir}/delete_{file_name}"
    shutil.copy(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)
    response = client.get(
        API_PREFIX + "/file/delete",
        params={"file_path": output_file_path},
        headers=test_headers,
    )
    assert not os.path.exists(output_file_path)

    print(response)
    assert response.status_code == 200
    data = response.json()
    assert "deleted successfully" in data["message"]
    print(data)


def test_delete_directory():
    output_test_dir = f"{output_dir}/delete_dir"
    shutil.copytree(input_dir, output_test_dir)
    assert os.path.exists(output_test_dir)
    response = client.get(
        API_PREFIX + "/file/delete_directory",
        params={"directory_path": output_test_dir},
        headers=test_headers,
    )
    assert not os.path.exists(output_test_dir)
    print(response)
    assert response.status_code == 200
    data = response.json()
    assert "deleted recursively successfully" in data["message"]
    print(data)
