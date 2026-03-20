from pydantic_settings import BaseSettings  # pip install pydantic-settings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-1.5-flash"  # Modelo Gemini actual (antes era text-bison PaLM)
    TIMEOUT: int = 10

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()