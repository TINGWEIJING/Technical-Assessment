from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import model, schema


def get_feature_by_id(
    db: Session,
    id: int
) -> Optional[model.Feature]:
    '''
    Retrieve single `Feature` data based on `id`.
    '''

    return db.query(model.Feature).filter(model.Feature.id == id).first()


def get_features(db: Session) -> List[model.Feature]:
    '''
    Retrieve all `Feature` data.
    '''

    return db.query(model.Feature).all()


def create_feature(
    db: Session,
    feature_create: schema.FeatureCreate
) -> model.Feature:
    '''
    Create single `Feature` data. \n
    Automatically insert many-to-many relationship records with all `User` data.
    '''

    users = db.query(model.User).all()

    new_feature = model.Feature(
        **jsonable_encoder(feature_create)
    )

    for user in users:
        new_feature.accessed_by.append(
            user
        )

    db.add(new_feature)
    db.commit()
    db.refresh(new_feature)
    return new_feature


def remove_feature(
    db: Session,
    id: int
) -> Optional[model.Feature]:
    '''
    Remove single `Feature` data.
    '''

    feature = db.get(
        model.Feature,
        id
    )

    if feature == None:
        return None

    db.delete(feature)
    db.commit()
    return feature
