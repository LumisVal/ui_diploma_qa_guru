import allure
from selene.support.shared import browser
from selene import have, be

from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.open("/login")
        return self

    @allure.step("Заполнить email: {email}")
    def fill_email(self, email):
        browser.element("#Email").set_value(email)
        return self

    @allure.step("Заполнить пароль")
    def fill_password(self, password):
        browser.element("#Password").set_value(password)
        return self

    @allure.step("Нажать кнопку Log in")
    def submit(self):
        browser.element(".login-button").click()
        return self

    @allure.step("Авторизоваться пользователем")
    def login(self, email, password):
        self.open_login_page()
        self.fill_email(email)
        self.fill_password(password)
        self.submit()
        return self

    @allure.step("Проверить ошибку авторизации")
    def should_have_login_error(self):
        browser.element(".validation-summary-errors").should(be.visible)
        browser.element(".validation-summary-errors").should(
            have.text("Login was unsuccessful")
        )
        return self

    @allure.step("Проверить успешную авторизацию")
    def should_be_logged_in(self, email):
        browser.element(".account").should(have.text(email))
        return self