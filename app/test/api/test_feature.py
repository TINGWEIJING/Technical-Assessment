from typing import Dict, List

import pytest
from fastapi import status

from app.test.conftest import client

# pytest.skip(allow_module_level=True) # TODO: comment out
URL_PREFIX = "/admin"


def test_get_features():
    response = client.get(
        f"{URL_PREFIX}/features/",
    )

    assert response.status_code == status.HTTP_200_OK

    data: List[Dict] = response.json()

    assert len(data) == 3

    single_data = data[0]
    assert single_data.get("id") != None
    assert single_data.get("name") != None


def test_get_feature():
    response = client.get(
        f"{URL_PREFIX}/features/1",
    )

    assert response.status_code == status.HTTP_200_OK

    data: Dict = response.json()

    assert data.get("id") == 1
    assert data.get("name") == "feature_01"


def test_get_feature_with_not_found():
    response = client.get(
        f"{URL_PREFIX}/features/100",
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_feature():
    response = client.post(
        f"{URL_PREFIX}/features/",
        json={
            "name": "feature_04"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED

    data: Dict = response.json()

    assert data.get("id") != None
    assert data.get("name") == "feature_04"


def test_create_feature_with_integrity_error():
    response = client.post(
        f"{URL_PREFIX}/features/",
        json={
            "name": "feature_01"  # already exists
        }
    )

    assert response.status_code == status.HTTP_409_CONFLICT


def test_delete_feature_with_ok():
    response = client.post(
        f"{URL_PREFIX}/features/",
        json={
            "name": "feature_05"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED

    new_feature: Dict = response.json()

    assert new_feature.get("id") != None
    assert new_feature.get("name") != None

    response = client.delete(
        f"{URL_PREFIX}/features/{new_feature.get('id')}",
    )

    assert response.status_code == status.HTTP_200_OK

    deleted_feature: Dict = response.json()

    assert deleted_feature.get("id") == new_feature.get("id")
    assert deleted_feature.get("name") == new_feature.get("name")


def test_delete_feature_with_conflict():
    response = client.delete(
        f"{URL_PREFIX}/features/10",
    )

    assert response.status_code == status.HTTP_409_CONFLICT
