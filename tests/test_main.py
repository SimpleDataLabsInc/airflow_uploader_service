#!/usr/bin/env python

"""Tests for `prophecy_pybridge` package."""

from fastapi.testclient import TestClient
from prophecy_pybridge.main import app

client = TestClient(app)


def test_hello():
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == {
        "Hello": "World"
    }

def test_upload():
    pass
