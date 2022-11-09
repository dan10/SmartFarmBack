from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "Smart Farm"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = 'mongodb+srv://dan10:<password>@sfcluster.qaaqyii.mongodb.net/?retryWrites=true&w=majority'
    DB_NAME: str = "farm"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
