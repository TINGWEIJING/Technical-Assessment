from typing import Dict, List

import pytest
from fastapi import status

from app.test.conftest import client

# pytest.skip(allow_module_level=True)  # TODO: comment out
URL_PREFIX = "/admin"


def test_get_users():
    response = client.get(
        f"{URL_PREFIX}/users/",
    )

    assert response.status_code == status.HTTP_200_OK

    data: List[Dict] = response.json()

    assert len(data) == 2

    single_data = data[0]
    assert single_data.get("id") != None
    assert single_data.get("email") != None


def test_get_user():
    response = client.get(
        f"{URL_PREFIX}/users/1",
    )

    assert response.status_code == status.HTTP_200_OK

    data: Dict = response.json()

    assert data.get("id") == 1
    assert data.get("email") == "user01@gmail.com"


def test_get_user_with_not_found():
    response = client.get(
        f"{URL_PREFIX}/users/100",
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_user():
    response = client.post(
        f"{URL_PREFIX}/users/",
        json={
            "email": "user03@gmail.com"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED

    data: Dict = response.json()

    assert data.get("id") != None
    assert data.get("email") == "user03@gmail.com"


def test_create_user_with_integrity_error():
    response = client.post(
        f"{URL_PREFIX}/users/",
        json={
            "email": "user01@gmail.com"  # already exists
        }
    )

    assert response.status_code == status.HTTP_409_CONFLICT


def test_delete_user_with_ok():
    response = client.post(
        f"{URL_PREFIX}/users/",
        json={
            "email": "user05@gmail.com"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED

    new_user: Dict = response.json()

    assert new_user.get("id") != None
    assert new_user.get("email") != None

    response = client.delete(
        f"{URL_PREFIX}/users/{new_user.get('id')}",
    )

    assert response.status_code == status.HTTP_200_OK

    deleted_user: Dict = response.json()

    assert deleted_user.get("id") == new_user.get("id")
    assert deleted_user.get("email") == new_user.get("email")


def test_delete_user_with_conflict():
    response = client.delete(
        f"{URL_PREFIX}/users/10",
    )

    assert response.status_code == status.HTTP_409_CONFLICT
