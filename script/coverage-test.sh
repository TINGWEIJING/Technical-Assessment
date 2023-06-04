#!/bin/sh

coverage run --source=app --omit="./app/main.py","./app/init_db.py" -m pytest -v "./app/test" \
  && coverage report -m

SQLALCHEMY_TEST_DATABASE_FILE=./database/test.db
if [ -f "$SQLALCHEMY_TEST_DATABASE_FILE" ]; then
    rm "$SQLALCHEMY_TEST_DATABASE_FILE"
fi
