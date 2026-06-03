import allure

from data.users import invalid_user, registered_user
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Login")
@allure.title("Unsuccessful login with invalid credentials")
def test_unsuccessful_login():
    login_page = LoginPage()

    login_page.open_login_page()
    login_page.fill_email(invalid_user.email)
    login_page.fill_password(invalid_user.password)
    login_page.submit()

    login_page.should_have_login_error()


@allure.feature("Login")
@allure.title("Successful login")
def test_successful_login():
    login_page = LoginPage()

    login_page.login(
        registered_user.email,
        registered_user.password
    )

    login_page.should_be_logged_in(
        registered_user.email
    )


@allure.feature("Logout")
@allure.title("Logout after successful login")
def test_logout():
    login_page = LoginPage()
    main_page = MainPage()

    login_page.login(
        registered_user.email,
        registered_user.password
    )

    main_page.logout()

    main_page.should_be_logged_out()