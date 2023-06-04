import pytest
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app import model, schema, service

# pytest.skip(allow_module_level=True)  # TODO: comment out


def test_get_feature_access_with_valid_return(
    db: Session,
):
    feature_access = service.get_feature_access(
        db=db,
        user_email="user01@gmail.com",
        feature_name="feature_01",
    )

    assert feature_access != None

    assert feature_access.feature_id == 1
    assert feature_access.user_id == 1
    assert feature_access.is_enabled == False


def test_get_feature_access_with_invalid_user(
    db: Session,
):
    feature_access = service.get_feature_access(
        db=db,
        user_email="user10@gmail.com",
        feature_name="feature_01",
    )

    assert feature_access == None


def test_get_feature_access_with_invalid_feature_access(
    db: Session,
):
    # remove the data
    deleted_feature_access = db.query(model.FeatureAccess).filter(and_(
        model.FeatureAccess.user_id == 2,
        model.FeatureAccess.feature_id == 2
    )).first()

    if deleted_feature_access != None:
        db.delete(deleted_feature_access)
        db.commit()

    feature_access = service.get_feature_access(
        db=db,
        user_email="user02@gmail.com",
        feature_name="feature_02",
    )

    assert feature_access == None


def test_update_feature_access_with_valid_return(
    db: Session,
):
    feature_access = service.update_feature_access(
        db=db,
        req_feature_access=schema.RequestUpdateFeatureAccess(
            featureName="feature_01",
            email="user02@gmail.com",
            enable=True,
        )
    )

    assert feature_access != None

    assert feature_access.feature_id == 1
    assert feature_access.user_id == 2
    assert feature_access.is_enabled == True


def test_update_feature_access_with_invalid_user(
    db: Session,
):
    feature_access = service.update_feature_access(
        db=db,
        req_feature_access=schema.RequestUpdateFeatureAccess(
            featureName="feature_01",
            email="user10@gmail.com",
            enable=True,
        )
    )

    assert feature_access == None


def test_update_feature_access_with_invalid_feature_access(
    db: Session,
):
    # remove the data
    deleted_feature_access = db.query(model.FeatureAccess).filter(and_(
        model.FeatureAccess.user_id == 2,
        model.FeatureAccess.feature_id == 2
    )).first()

    if deleted_feature_access != None: # pragma: nocover
        db.delete(deleted_feature_access)
        db.commit()

    feature_access = service.update_feature_access(
        db=db,
        req_feature_access=schema.RequestUpdateFeatureAccess(
            featureName="feature_02",
            email="user02@gmail.com",
            enable=True,
        )
    )

    assert feature_access == None
