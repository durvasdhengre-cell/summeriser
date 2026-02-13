from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODEL_PATH: str = "model/medical_model"

settings = Settings()
