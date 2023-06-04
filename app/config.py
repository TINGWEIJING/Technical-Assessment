from pydantic import BaseSettings


class Settings(BaseSettings):
    '''
    Contains environment variables for server settings. \n
    Values will be overriden automatically if `.env` file exists.
    '''

    APP_NAME: str = "MoneyLion Technical Assessment"
    INIT_DATA_FILE: str = "./data/init_data.json"
    INIT_TEST_DATA_FILE: str = "./data/test_data.json"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./database/app.db"
    SQLALCHEMY_TEST_DATABASE_URL: str = "sqlite:///./database/test.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
