import allure

from data.users import random_user
from pages.register_page import RegisterPage


@allure.feature("Registration")
@allure.title("Successful user registration")
def test_successful_registration():
    user = random_user()

    register_page = RegisterPage()

    register_page.open_register_page()
    register_page.fill_registration_form(
        user.first_name,
        user.last_name,
        user.email,
        user.password,
    )
    register_page.submit()
    register_page.should_be_registered()