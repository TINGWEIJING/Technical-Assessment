#!/bin/sh

python -m app.init_db ./app/init_db.py

uvicorn app.main:app --host "0.0.0.0" --port 80