from selene.support.shared import browser


class BasePage:
    def open(self, path="/"):
        browser.open(path)
        return self