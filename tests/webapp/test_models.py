import pytest

from webapp.app import create_app, app
from webapp.settings import TestConfig

@pytest.fixture
def app():
    app = create_app(app, TestConfig)
    return app


def test_db_table_country():
    assert True

def test_db_table_location():
    assert True

def test_api_location():
    assert True

def test_api_target():
    assert True
