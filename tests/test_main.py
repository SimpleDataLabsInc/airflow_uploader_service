#!/usr/bin/env python

"""Tests for `prophecy_pybridge` package."""
import io
import os

from fastapi.testclient import TestClient
from prophecy_pybridge.main import app

client = TestClient(app)


def test_hello():
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello Prophecy!'}


def test_name():
    response = client.get('/hello', params={"name": "Ashish"})
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello Ashish!'}


def test_upload_file():
    # Use TestClient to interact with your FastAPI app
    # Open a file to simulate uploading
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = "test.txt"
    input_file_path = current_file_dir + f"/resources/input/{file_name}"
    output_dir = current_file_dir + f"/resources/output"
    output_file_path=f"f{output_dir}/{file_name}"
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        print(f"Test File {output_file_path} removed successfully.")
    else:
        print(f"File {output_file_path} does not exist.")

    # Read the content of the test file
    with open(input_file_path, "rb") as file:
        file_content = file.read()
        # Use requests.post to simulate the file upload
        response = client.post("/upload",
                               params={"destination_dir": output_dir},
                               files={"file": (file_name, file_content)}
                               )
        print(response)
        # Assert the response is successful (status code 200)
        assert response.status_code == 200
        # Assert the response contains the expected data
        data = response.json()
        assert data["filename"] == "test.txt"
        assert output_dir in data["file_path"]
