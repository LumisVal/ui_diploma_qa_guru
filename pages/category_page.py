import allure
from selene.support.shared import browser
from selene import have, be

from pages.base_page import BasePage


class CategoryPage(BasePage):

    @allure.step("Открыть категорию Computers")
    def open_computers_category(self):
        self.open("/computers")
        return self

    @allure.step("Открыть категорию Desktops")
    def open_desktops_category(self):
        self.open("/desktops")
        return self

    @allure.step("Проверить заголовок категории: {title}")
    def should_have_category_title(self, title):
        browser.element(".page-title").should(
            have.text(title)
        )
        return self

    @allure.step("Проверить наличие товаров")
    def should_have_products(self):
        browser.element(".product-grid").should(
            be.visible
        )
        return self

    @allure.step("Открыть товар: {product_name}")
    def open_product(self, product_name):
        browser.all(".product-title").element_by(
            have.text(product_name)
        ).click()
        return self

    @allure.step("Открыть товар: {product_name}")
    def open_product(self, product_name):
        browser.all(".product-title").element_by(
            have.text(product_name)
        ).click()
        return self

    @allure.step("Проверить, что список товаров отображается")
    def should_have_products(self):
        browser.element(".product-grid").should(be.visible)
        return self