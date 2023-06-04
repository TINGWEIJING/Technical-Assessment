from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import model, schema


def get_user_by_id(
    db: Session,
    id: int
) -> Optional[model.User]:
    '''
    Retrieve single `Feature` data based on `id`.
    '''

    return db.query(model.User).filter(model.User.id == id).first()


def get_users(db: Session) -> List[model.User]:
    '''
    Retrieve all `Feature` data.
    '''

    return db.query(model.User).all()


def create_user(
    db: Session,
    user_create: schema.UserCreate
) -> model.User:
    '''
    Create single `User` data. \n
    Automatically insert many-to-many relationship records with all `Feature` data.
    '''

    features = db.query(model.Feature).all()

    new_user = model.User(
        **jsonable_encoder(user_create)
    )
    for feature in features:
        new_user.accessible_features.append(
            feature
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def remove_user(
    db: Session,
    id: int
) -> Optional[model.User]:
    '''
    Remove single `User` data.
    '''

    user = db.get(
        model.User,
        id
    )

    if user == None:
        return None

    db.delete(user)
    db.commit()
    return user
