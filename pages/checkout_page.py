import allure
from selene import have
from selene.support.shared import browser
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    @allure.step("Принять условия обслуживания")
    def accept_terms(self):
        browser.element("#termsofservice").click()
        return self

    @allure.step("Перейти к оформлению заказа")
    def checkout(self):
        browser.element("#checkout").click()
        return self

    @allure.step("Заполнить Billing Address")
    def fill_billing_address(self):
        Select(
            browser.element("#BillingNewAddress_CountryId").locate()
        ).select_by_visible_text("United States")

        browser.element("#BillingNewAddress_City").set_value("New York")
        browser.element("#BillingNewAddress_Address1").set_value("Wall Street 1")
        browser.element("#BillingNewAddress_ZipPostalCode").set_value("10001")
        browser.element("#BillingNewAddress_PhoneNumber").set_value("1234567890")

        return self

    @allure.step("Продолжить Billing Address")
    def continue_billing_address(self):
        browser.element("[onclick='Billing.save()']").click()
        return self

    @allure.step("Продолжить Shipping Address")
    def continue_shipping_address(self):
        browser.element("#shipping-buttons-container input.button-1").click()
        return self

    @allure.step("Продолжить Shipping Method")
    def continue_shipping_method(self):
        browser.element("#shipping-method-buttons-container input.button-1").click()
        return self

    @allure.step("Продолжить Payment Method")
    def continue_payment_method(self):
        browser.element("#payment-method-buttons-container input.button-1").click()
        return self

    @allure.step("Продолжить Payment Information")
    def continue_payment_information(self):
        browser.element("#payment-info-buttons-container input.button-1").click()
        return self

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        browser.element("#confirm-order-buttons-container input.button-1").click()
        return self

    @allure.step("Проверить успешное оформление заказа")
    def should_have_successful_order_message(self):
        browser.element(".title").should(
            have.text("Your order has been successfully processed!")
        )
        return self