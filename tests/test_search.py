import allure

from pages.main_page import MainPage
from pages.search_page import SearchPage


@allure.feature("Search")
@allure.title("Search existing product")
def test_search_existing_product():
    main_page = MainPage()
    search_page = SearchPage()

    main_page.open_main_page()
    main_page.search_product("computer")

    search_page.should_have_product("Build your own computer")


@allure.feature("Search")
@allure.title("Search nonexistent product")
def test_search_nonexistent_product():
    main_page = MainPage()
    search_page = SearchPage()

    main_page.open_main_page()
    main_page.search_product("qwerty-not-existing-product")

    search_page.should_have_no_results_message()