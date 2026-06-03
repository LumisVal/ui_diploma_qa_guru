from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_url: str = "https://demowebshop.tricentis.com"
    browser_name: str = "chrome"
    browser_width: int = 1920
    browser_height: int = 1080
    timeout: int = 8

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()