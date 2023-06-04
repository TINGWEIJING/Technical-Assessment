from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import exc
from sqlalchemy.orm import Session

from app import schema, service
from app.db.session import get_db

router = APIRouter()


@router.get("/users/", response_model=List[schema.ResponseUser])
def get_users(
    db: Session = Depends(get_db),
):
    users = service.get_users(db=db)
    return users


@router.get("/users/{id}", response_model=schema.ResponseUser)
def get_user(
    id: int,
    db: Session = Depends(get_db),
):
    user = service.get_user_by_id(
        db=db,
        id=id
    )

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found.")

    return user


@router.post("/users/", response_model=schema.ResponseUser, status_code=status.HTTP_201_CREATED)
def create_user(
    user_create: schema.UserCreate,
    db: Session = Depends(get_db),
):
    try:
        user = service.create_user(
            db=db,
            user_create=user_create,
        )

        return user
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Failed to create user, user email already exists.")


@router.delete("/users/{id}", response_model=schema.ResponseUser)
def delete_user(
    id: int,
    db: Session = Depends(get_db),
):
    user = service.remove_user(
        db=db,
        id=id,
    )

    if user == None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Failed to delete user.")

    return user
