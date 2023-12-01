#!/usr/bin/env python

"""Tests for `prophecy_pybridge` package."""

from fastapi.testclient import TestClient
from prophecy_pybridge.main import app, API_PREFIX

client = TestClient(app)
def test_hello():
    response = client.get(API_PREFIX + "/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Prophecy!"}


def test_name():
    response = client.get(API_PREFIX + "/hello", params={"name": "Ashish"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Ashish!"}



