import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api import api_router
from app.config import settings
from app.db.init_data import init_data
from app.db.session import Base, get_db

engine = create_engine(
    settings.SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.drop_all(bind=engine)  # drop all tables
Base.metadata.create_all(bind=engine)  # create all tables
is_data_init = False


def override_get_db():
    '''
    A method to override the implementation of `get_db()` dependency used by API endpoints.
    '''

    global is_data_init

    try:
        db = TestingSessionLocal()
        if not is_data_init:
            init_data(
                db=db,
                json_file=settings.INIT_TEST_DATA_FILE
            )
            is_data_init = True
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def db():
    '''
    Injecting database connection session through `pytest.fixture`.
    '''

    yield next(override_get_db())


app = FastAPI()
app.dependency_overrides[get_db] = override_get_db
app.include_router(api_router)

client = TestClient(app)
