from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


ORIGINAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities = deepcopy(ORIGINAL_ACTIVITIES)
    yield
    app_module.activities = deepcopy(ORIGINAL_ACTIVITIES)


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client
