from typing import Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app import model, schema


def get_feature_access(
    db: Session,
    user_email: str,
    feature_name: str
) -> Optional[model.FeatureAccess]:
    '''
    Retrieve single `FeatureAccess` data based on `user.email` and `feature.name`.
    '''

    user = db.query(
        model.User
    ).filter(
        model.User.email == user_email
    ).first()

    feature = db.query(
        model.Feature
    ).filter(
        model.Feature.name == feature_name
    ).first()

    if user == None or feature == None:
        return None

    feature_access = db.query(model.FeatureAccess).filter(and_(
        model.FeatureAccess.user_id == user.id,
        model.FeatureAccess.feature_id == feature.id
    )).first()

    if feature_access == None:
        return None

    return feature_access


def update_feature_access(
        db: Session,
        req_feature_access:
        schema.RequestUpdateFeatureAccess
) -> Optional[model.FeatureAccess]:
    '''
    Update single `FeatureAccess` data. Return `None` if the target data does not exist.
    '''

    user = db.query(
        model.User
    ).filter(
        model.User.email == req_feature_access.email
    ).first()

    feature = db.query(
        model.Feature
    ).filter(
        model.Feature.name == req_feature_access.featureName
    ).first()

    if user == None or feature == None:
        return None

    feature_access = db.query(model.FeatureAccess).filter(and_(
        model.FeatureAccess.user_id == user.id,
        model.FeatureAccess.feature_id == feature.id
    )).first()

    if feature_access == None:
        return None
    feature_access.is_enabled = req_feature_access.enable

    db.commit()

    return feature_access
