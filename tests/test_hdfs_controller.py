#!/usr/bin/env python

"""Tests for `prophecy_pybridge` package."""
import json
import os

from fastapi.testclient import TestClient
from prophecy_pybridge.controller.hdfs_controller import HdfsController

from prophecy_pybridge.main import app, API_PREFIX
from . import test_headers

client = TestClient(app)
current_file_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "test.txt"
input_dir = current_file_dir + "/resources/input"
input_file_path = input_dir + f"/{file_name}"
output_hdfs_dir = "/pateash"
test_hdfs_file_path = output_hdfs_dir + "/" + file_name


# only run in local can't run this on CI/CD, as we don't have hadoop/hdfs installed there.


def test_hdfs_all():
    if "ashishpatel" in os.environ["HOME"]:
        t_upload_file()
        t_delete_file()
        t_delete_dir()
    else:
        print("SKIP: hadoop tests.")


def t_upload_file():
    print("\n\nTESTING UPLOAD FILE")
    # first remove and then try this
    with open(input_file_path, "rb") as file:
        file_content = file.read()
        response = client.post(
            API_PREFIX + "/hdfs/upload",
            params={"destination_dir": output_hdfs_dir},
            files={"file": (file_name, file_content)},
            headers=test_headers,
        )
        data = response.json()
        print(json.dumps(data, indent=2))

        assert response.status_code == 200
        assert "test.txt" in data["message"]


def t_delete_file():
    print("\n\nTESTING DELETE FILE")
    response = client.get(
        API_PREFIX + "/hdfs/delete",
        params={"file_path": test_hdfs_file_path},
        headers=test_headers,
    )
    data = response.json()
    print(json.dumps(data, indent=2))
    assert response.status_code == 200
    assert "removed successfully" in data["message"]


def t_delete_dir():
    print("\n\nTESTING DELETE DIRECTORY Feature recursively")
    test_hdfs_dir_path = "/pateash/rmdir-test"
    HdfsController.run_cmd(f"hdfs dfs -mkdir -p {test_hdfs_dir_path}")
    response = client.get(
        API_PREFIX + "/hdfs/delete_directory",
        params={"directory_path": test_hdfs_dir_path},
        headers=test_headers,
    )

    data = response.json()
    print(json.dumps(data, indent=2))
    assert response.status_code == 200
    assert "has been recursively removed" in data["message"]
