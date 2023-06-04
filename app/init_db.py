import logging

from app.config import settings

from . import model
from .db.init_data import init_data
from .db.session import SessionLocal, engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    '''
    Initialize the sqlite database with data loaded from json file.
    '''

    logger.info(f"Creating initial data from {settings.INIT_DATA_FILE}")
    db = SessionLocal()
    metadata = model.Base.metadata
    metadata.create_all(bind=engine)
    is_init_succeed = init_data(db, settings.INIT_DATA_FILE)

    if is_init_succeed:
        logger.info("Initial data created")
    else:
        logger.info("Database is not empty.")


def main() -> None:
    init()


if __name__ == "__main__":
    main()
