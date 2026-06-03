import allure
from selene.support.shared import browser
from selene import have

from pages.base_page import BasePage


class RegisterPage(BasePage):

    @allure.step("Открыть страницу регистрации")
    def open_register_page(self):
        self.open("/register")
        return self

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, first_name, last_name, email, password):
        browser.element("#gender-male").click()
        browser.element("#FirstName").set_value(first_name)
        browser.element("#LastName").set_value(last_name)
        browser.element("#Email").set_value(email)
        browser.element("#Password").set_value(password)
        browser.element("#ConfirmPassword").set_value(password)
        return self

    @allure.step("Отправить форму регистрации")
    def submit(self):
        browser.element("#register-button").click()
        return self

    @allure.step("Проверить успешную регистрацию")
    def should_be_registered(self):
        browser.element(".result").should(have.text("Your registration completed"))
        return self

    @allure.step("Выйти после регистрации")
    def logout_after_registration(self):
        browser.element(".ico-logout").click()
        return self