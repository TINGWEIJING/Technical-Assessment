import json

from sqlalchemy.orm import Session

from app import model, schema, service


def init_data(db: Session, json_file: str) -> bool:
    '''
    Insert sample data into sqlite database if the database is empty.
    '''

    # check database already has data
    users = service.get_users(db=db)
    features = service.get_features(db=db)

    # do nothing if data exists
    if len(users) > 0 or len(features) > 0: # pragma: nocover
        return False

    # read json file
    with open(json_file, 'r') as f:
        raw_data: dict = json.load(f)
        raw_features = raw_data.get("features")
        raw_users = raw_data.get("users")

        # process feature model
        db.bulk_save_objects(
            [model.Feature(name=raw_feature["name"]) for raw_feature in raw_features]
        )
        db.commit()

        # process user model
        for raw_user in raw_users:
            service.create_user(
                db=db,
                user_create=schema.UserCreate(
                    email=raw_user["email"]
                )
            )
        return True
