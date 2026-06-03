import os

import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from config.settings import settings
from utils import attachments


def is_remote():
    return os.getenv("REMOTE", "false").lower() == "true"


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = settings.base_url
    browser.config.timeout = settings.timeout
    browser.config.window_width = settings.browser_width
    browser.config.window_height = settings.browser_height

    options = Options()

    if is_remote():
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            },
        }

        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability(
            "selenoid:options",
            selenoid_capabilities["selenoid:options"],
        )

        browser.config.driver_remote_url = os.getenv(
            "SELENOID_URL",
            "https://user1:1234@selenoid.autotests.cloud/wd/hub",
        )
        browser.config.driver_options = options

    else:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={settings.browser_width},{settings.browser_height}")

        browser.config.driver_options = options
        browser.config.browser_name = settings.browser_name

    yield

    attachments.add_screenshot()
    attachments.add_html()
    attachments.add_logs()

    browser.quit()