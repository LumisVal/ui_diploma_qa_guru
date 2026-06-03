import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    base_url = os.getenv(
        "BASE_URL",
        "https://demowebshop.tricentis.com",
    )
    browser_name = os.getenv("BROWSER_NAME", "chrome")
    browser_width = int(os.getenv("BROWSER_WIDTH", "1920"))
    browser_height = int(os.getenv("BROWSER_HEIGHT", "1080"))
    timeout = int(os.getenv("TIMEOUT", "8"))


settings = Settings()