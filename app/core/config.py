from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    database_url: str
    description: str
    secret: str = 'extra gin'

    class Config:
        env_file = '../.env'


settings = Settings()
