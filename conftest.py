import pytest
from selene.support.shared import browser

from config.settings import settings
from utils import attachments


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = settings.base_url
    browser.config.browser_name = settings.browser_name
    browser.config.window_width = settings.browser_width
    browser.config.window_height = settings.browser_height
    browser.config.timeout = settings.timeout

    yield

    attachments.add_screenshot()
    attachments.add_html()
    attachments.add_logs()

    browser.quit()