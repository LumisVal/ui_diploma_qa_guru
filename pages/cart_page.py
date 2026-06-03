import allure
from selene.support.shared import browser
from selene import have, be

from pages.base_page import BasePage


class CartPage(BasePage):

    @allure.step("Открыть страницу товара")
    def open_product_page(self, product_url):
        self.open(product_url)
        return self

    @allure.step("Добавить товар в корзину")
    def add_product_to_cart(self):
        browser.element(".product-essential .add-to-cart-button").click()

        browser.element(".bar-notification.success").should(
            have.text("The product has been added to your shopping cart")
        )

        return self

    @allure.step("Открыть корзину")
    def open_cart(self):
        browser.element(".bar-notification.success .close").click()
        browser.element(".cart-label").click()
        return self

    @allure.step("Проверить товар в корзине: {product_name}")
    def should_have_product_in_cart(self, product_name):
        browser.element(".product-name").should(
            have.text(product_name)
        )
        return self

    @allure.step("Очистить корзину")
    def remove_product_from_cart(self):
        browser.element("input[name='removefromcart']").click()
        browser.element(".update-cart-button").click()
        return self

    @allure.step("Проверить, что корзина пустая")
    def should_be_empty(self):
        browser.element(".order-summary-content").should(
            have.text("Your Shopping Cart is empty!")
        )
        return self