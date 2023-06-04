import pytest
from sqlalchemy.orm import Session

from app import schema, service

# pytest.skip(allow_module_level=True)  # TODO: comment out


def test_get_feature_by_id_with_valid_return(
    db: Session,
):
    feature = service.get_feature_by_id(
        db=db,
        id=1,
    )

    assert feature != None

    assert feature.id == 1
    assert feature.name == "feature_01"


def test_get_feature_by_id_with_invalid_id(
    db: Session,
):
    feature = service.get_feature_by_id(
        db=db,
        id=10,
    )

    assert feature == None


def test_get_features(
    db: Session,
):
    features = service.get_features(
        db=db,
    )

    assert len(features) > 0

    feature = features[0]

    assert feature.id != 0
    assert len(feature.name) > 0


def test_create_feature(
    db: Session,
):
    feature = service.create_feature(
        db=db,
        feature_create=schema.FeatureCreate(
            name="feature_11",
        ),
    )

    assert feature != None

    assert feature.id > 0
    assert feature.name == "feature_11"


def test_remove_feature_with_valid_return(
    db: Session,
):
    # insert the data
    to_delete_feature = service.create_feature(
        db=db,
        feature_create=schema.FeatureCreate(
            name="feature_05",
        ),
    )

    deleted_feature = service.remove_feature(
        db=db,
        id=to_delete_feature.id,
    )

    assert deleted_feature != None
    assert deleted_feature.id == to_delete_feature.id
    assert deleted_feature.name == to_delete_feature.name


def test_remove_feature_with_invalid_id(
    db: Session,
):
    deleted_feature = service.remove_feature(
        db=db,
        id=10,  # not exist
    )

    assert deleted_feature == None
