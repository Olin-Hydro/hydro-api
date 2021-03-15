import os
import tempfile

import pytest

from app import create_app

@pytest.fixture
def app():
    yield create_app(env="test")

@pytest.fixture
def test_client(app):
    return app.test_client()
