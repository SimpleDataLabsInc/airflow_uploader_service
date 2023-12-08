#!/usr/bin/env python

"""Tests for `airflow_uploader_service` package."""

from fastapi.testclient import TestClient

from airflow_uploader_service.main import app, API_PREFIX
from . import test_headers

client = TestClient(app)


def test_hello():
    response = client.get(API_PREFIX + "/hello", headers=test_headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Prophecy!"}


def test_name():
    response = client.get(
        API_PREFIX + "/hello", params={"name": "Ashish"}, headers=test_headers
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Ashish!"}


def test_without_auth():
    response = client.get(API_PREFIX + "/hello", params={"name": "Ashish"})
    assert response.status_code == 401
    assert response.json() == {"message": "Access Denied"}
