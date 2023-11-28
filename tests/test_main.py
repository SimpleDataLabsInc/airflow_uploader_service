#!/usr/bin/env python

"""Tests for `prophecy_pybridge` package."""
import io
import os
import shutil

from fastapi.testclient import TestClient
from prophecy_pybridge.main import app

client = TestClient(app)
current_file_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "test.txt"
input_file_path = current_file_dir + f"/resources/input/{file_name}"
output_dir = current_file_dir + "/resources/output"


def test_hello():
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello Prophecy!'}


def test_name():
    response = client.get('/hello', params={"name": "Ashish"})
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello Ashish!'}


def test_upload_file():
    output_file_path = f"{output_dir}/{file_name}"
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        print(f"Test File {output_file_path} removed successfully.")
    else:
        print(f"File {output_file_path} does not exist.")

    with open(input_file_path, "rb") as file:
        file_content = file.read()
        response = client.post("/upload",
                               params={"destination_dir": output_dir},
                               files={"file": (file_name, file_content)}
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
    response = client.get("/delete",
                               params={"file_path": output_file_path},
                               )
    assert not os.path.exists(output_file_path)

    # print(response)
    assert response.status_code == 200
    data = response.json()
    assert " deleted successfully" in data["message"]
    # print(data)
