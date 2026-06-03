import allure
from allure_commons.types import AttachmentType
from selene.support.shared import browser


def add_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=AttachmentType.PNG,
    )


def add_html():
    allure.attach(
        browser.driver.page_source,
        name="Page source",
        attachment_type=AttachmentType.HTML,
    )


def add_logs():
    try:
        logs = browser.driver.get_log("browser")
        allure.attach(
            str(logs),
            name="Browser logs",
            attachment_type=AttachmentType.TEXT,
        )
    except Exception:
        pass