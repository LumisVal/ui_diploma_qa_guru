import allure
from selene.support.shared import browser
from selene import have, be


class ProductPage:

    @allure.step("Проверить название товара: {product_name}")
    def should_have_product_title(self, product_name):
        browser.element(".product-name").should(
            have.text(product_name)
        )
        return self

    @allure.step("Проверить, что цена товара отображается")
    def should_have_price(self):
        browser.element(".product-price").should(be.visible)
        return self

    @allure.step("Проверить, что кнопка Add to cart отображается")
    def should_have_add_to_cart_button(self):
        browser.element(".add-to-cart-button").should(be.visible)
        return self