import os 
from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings:
    PROJECT_NAME:str = "Capstone Project"
    API_KEY : str = os.getenv("API_KEY","DEMO_KEY")
    JWT_SECRET_KEY : str = os.getenv("JWT_SECRET_KEY","SECRET_KEY")
    JWT_ALGORITHM : str = "HS256"
    REDIS_URL : str = os.getemv("REDIS_URL", "redis:/localhost:6379")
    MODEL_PATH : str = "app/model/model.pkl"


def get_settings():
    return Settings()
