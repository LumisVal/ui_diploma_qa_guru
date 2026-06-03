import allure
from selene.support.shared import browser
from selene import have

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open("/")
        return self

    @allure.step("Перейти на страницу авторизации")
    def go_to_login_page(self):
        browser.element(".ico-login").click()
        return self

    @allure.step("Перейти на страницу регистрации")
    def go_to_register_page(self):
        browser.element(".ico-register").click()
        return self

    @allure.step("Выполнить поиск товара: {query}")
    def search_product(self, query):
        browser.element("#small-searchterms").type(query).press_enter()
        return self

    @allure.step("Проверить, что пользователь не авторизован")
    def should_have_login_link(self):
        browser.element(".ico-login").should(have.text("Log in"))
        return self

    @allure.step("Выйти из аккаунта")
    def logout(self):
        browser.element(".ico-logout").click()
        return self

    @allure.step("Проверить, что пользователь авторизован")
    def should_be_logged_in(self, email):
        browser.element(".account").should(
            have.text(email)
        )
        return self

    @allure.step("Проверить, что пользователь вышел")
    def should_be_logged_out(self):
        browser.element(".ico-login").should(
            have.text("Log in")
        )
        return self