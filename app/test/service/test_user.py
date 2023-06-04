import pytest
from sqlalchemy.orm import Session

from app import schema, service

# pytest.skip(allow_module_level=True)  # TODO: comment out


def test_get_user_by_id_with_valid_return(
    db: Session,
):
    user = service.get_user_by_id(
        db=db,
        id=1,
    )

    assert user != None

    assert user.id == 1
    assert user.email == "user01@gmail.com"


def test_get_user_by_id_with_invalid_id(
    db: Session,
):
    user = service.get_user_by_id(
        db=db,
        id=10,
    )

    assert user == None


def test_get_users(
    db: Session,
):
    users = service.get_users(
        db=db,
    )

    assert len(users) > 0

    user = users[0]

    assert user.id != 0
    assert len(user.email) > 0


def test_create_user(
    db: Session,
):
    user = service.create_user(
        db=db,
        user_create=schema.UserCreate(
            email="user11@gmail.com",
        ),
    )

    assert user != None

    assert user.id > 0
    assert user.email == "user11@gmail.com"


def test_remove_user_with_valid_return(
    db: Session,
):
    # insert the data
    to_delete_user = service.create_user(
        db=db,
        user_create=schema.UserCreate(
            email="user04@gmail.com",
        ),
    )

    deleted_user = service.remove_user(
        db=db,
        id=to_delete_user.id,
    )

    assert deleted_user != None
    assert deleted_user.id == to_delete_user.id
    assert deleted_user.email == to_delete_user.email


def test_remove_user_with_invalid_id(
    db: Session,
):
    deleted_user = service.remove_user(
        db=db,
        id=10,  # not exist
    )

    assert deleted_user == None
