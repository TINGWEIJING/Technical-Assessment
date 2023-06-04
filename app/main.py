from fastapi import FastAPI
from sqlalchemy import MetaData

from app import model
from app.api import api_router
from app.config import settings
from app.db.session import engine

metadata: MetaData = model.Base.metadata

metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "Requirement",
        "description": "The required API endpoints from technical assessment.",
    },
    {
        "name": "user",
        "description": "Operations with users.",
    },
    {
        "name": "feature",
        "description": "Operations with features.",
    },
]

app = FastAPI(
    title=settings.APP_NAME,
    description="""
A REST API server developed by TING WEI JING for MoneyLion technical assessment.\n
## Default Data in Database
- **All feature accesses are not enabled by default in the database.**

### `user` table
| id  | email            |
| --- | ---------------- |
| 1   | thomas@gmail.com |
| 2   | leo@gmail.com    |
| 3   | ali@gmail.com    |


### `feature` table
| id  | name            |
| --- | --------------- |
| 1   | Dark theme UI   |
| 2   | Multi-tab       |
| 3   | Export to PDF   |
| 4   | Import from CSV |
""",

    contact={
        "name": "TING WEI JING",
        "url": "https://github.com/TINGWEIJING",
        "email": "tingweijingting2000@gmail.com",
    },
    openapi_tags=tags_metadata,
)

app.include_router(api_router)
