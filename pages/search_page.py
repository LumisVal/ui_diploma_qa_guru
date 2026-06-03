import allure
from selene.support.shared import browser
from selene import have, be


class SearchPage:

    @allure.step("Проверить, что в результатах есть товар: {product_name}")
    def should_have_product(self, product_name):
        browser.element(".product-grid").should(be.visible)
        browser.element(".product-grid").should(have.text(product_name))
        return self

    @allure.step("Проверить сообщение об отсутствии результатов")
    def should_have_no_results_message(self):
        browser.element(".search-results").should(
            have.text("No products were found")
        )
        return self