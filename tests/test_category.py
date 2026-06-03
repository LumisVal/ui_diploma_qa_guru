import allure

from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@allure.feature("Catalog")
@allure.title("Open computers category")
def test_open_computers_category():
    category_page = CategoryPage()

    category_page.open_computers_category()
    category_page.should_have_category_title("Computers")


@allure.feature("Catalog")
@allure.title("Open desktops category")
def test_open_desktops_category():
    category_page = CategoryPage()

    category_page.open_computers_category()
    category_page.open_desktops_category()
    category_page.should_have_category_title("Desktops")
    category_page.should_have_products()


@allure.feature("Product")
@allure.title("Open product card from category")
def test_open_product_card_from_category():
    category_page = CategoryPage()
    product_page = ProductPage()

    category_page.open_computers_category()
    category_page.open_desktops_category()
    category_page.open_product("Build your own cheap computer")

    product_page.should_have_product_title("Build your own cheap computer")
    product_page.should_have_price()
    product_page.should_have_add_to_cart_button()