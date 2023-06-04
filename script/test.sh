#!/bin/sh

pytest -s -v "./app/test"

SQLALCHEMY_TEST_DATABASE_FILE=./database/test.db
if [ -f "$SQLALCHEMY_TEST_DATABASE_FILE" ]; then
    rm "$SQLALCHEMY_TEST_DATABASE_FILE"
fi
