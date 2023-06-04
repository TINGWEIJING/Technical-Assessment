import pytest
from fastapi import status

from app.test.conftest import client

# pytest.skip(allow_module_level=True) # TODO: comment out

def test_get_can_user_access_feature_with_enable_is_false():
    response = client.get(
        "/feature",
        params={
            "email": "user01@gmail.com",
            "featureName": "feature_01",
        }
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["canAccess"] == False


def test_get_can_user_access_feature_with_enable_is_true():
    # modify the data
    response = client.post(
        "/feature",
        json={
            "featureName": "feature_02",
            "email": "user01@gmail.com",
            "enable": True,
        }
    )

    assert response.status_code == status.HTTP_200_OK

    response = client.get(
        "/feature",
        params={
            "email": "user01@gmail.com",
            "featureName": "feature_02",
        }
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["canAccess"] == True


def test_get_can_user_access_feature_with_not_found():
    response = client.get(
        "/feature",
        params={
            "email": "user01@gmail.com",
            "featureName": "feature_05",
        }
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_access_feature_with_ok():
    response = client.post(
        "/feature",
        json={
            "featureName": "feature_02",
            "email": "user01@gmail.com",
            "enable": True,
        }
    )

    assert response.status_code == status.HTTP_200_OK


def test_update_access_feature_with_not_modified():
    response = client.post(
        "/feature",
        json={
            "featureName": "feature_10",
            "email": "user01@gmail.com",
            "enable": True,
        }
    )

    assert response.status_code == status.HTTP_304_NOT_MODIFIED
