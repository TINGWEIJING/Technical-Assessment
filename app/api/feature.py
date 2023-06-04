from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import exc
from sqlalchemy.orm import Session

from app import schema, service
from app.db.session import get_db

router = APIRouter()


@router.get("/features/", response_model=List[schema.ResponseFeature])
def get_features(
    db: Session = Depends(get_db),
):
    features = service.get_features(
        db=db
    )
    return features


@router.get("/features/{id}", response_model=schema.ResponseFeature)
def get_feature(
    id: int,
    db: Session = Depends(get_db),
):
    feature = service.get_feature_by_id(
        db=db,
        id=id
    )

    if feature == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Feature not found.")

    return feature


@router.post("/features/", response_model=schema.ResponseFeature, status_code=status.HTTP_201_CREATED)
def create_feature(
    feature_create: schema.FeatureCreate,
    db: Session = Depends(get_db),
):
    try:
        feature = service.create_feature(
            db=db,
            feature_create=feature_create,
        )

        return feature
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Failed to create feature, feature name already exists.")


@router.delete("/features/{id}", response_model=schema.ResponseFeature)
def delete_feature(
    id: int,
    db: Session = Depends(get_db),
):
    feature = service.remove_feature(
        db=db,
        id=id,
    )

    if feature == None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Failed to delete feature.")

    return feature
