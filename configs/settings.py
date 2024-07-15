from pydantic import Field
from pydantic_settings import BaseSettings

#criar configurações da API

class Settings(BaseSettings):
    DB_URL: str = Field(default= 'postgresql+asyncpg://workout:workout@localhost/workout')


settings = Settings()