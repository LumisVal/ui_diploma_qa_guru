import allure

from data.users import random_user
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@allure.feature("Checkout")
@allure.title("New registered user can checkout product")
def test_new_registered_user_can_checkout_product():
    user = random_user()

    register_page = RegisterPage()
    login_page = LoginPage()
    cart_page = CartPage()
    checkout_page = CheckoutPage()

    register_page.open_register_page()
    register_page.fill_registration_form(
        user.first_name,
        user.last_name,
        user.email,
        user.password,
    )
    register_page.submit()
    register_page.should_be_registered()
    register_page.logout_after_registration()

    login_page.login(
        user.email,
        user.password,
    )

    cart_page.open_product_page("/build-your-cheap-own-computer")
    cart_page.add_product_to_cart()
    cart_page.open_cart()

    checkout_page.accept_terms()
    checkout_page.checkout()

    checkout_page.fill_billing_address()
    checkout_page.continue_billing_address()

    checkout_page.continue_shipping_address()
    checkout_page.continue_shipping_method()
    checkout_page.continue_payment_method()
    checkout_page.continue_payment_information()

    checkout_page.confirm_order()
    checkout_page.should_have_successful_order_message()