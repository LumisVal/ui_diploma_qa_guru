import allure

from pages.cart_page import CartPage


@allure.feature("Cart")
@allure.title("Add product to cart")
def test_add_product_to_cart():
    cart_page = CartPage()

    cart_page.open_product_page("/build-your-cheap-own-computer")
    cart_page.add_product_to_cart()
    cart_page.open_cart()

    cart_page.should_have_product_in_cart(
        "Build your own cheap computer"
    )


@allure.feature("Cart")
@allure.title("Remove product from cart")
def test_remove_product_from_cart():
    cart_page = CartPage()

    cart_page.open_product_page("/build-your-cheap-own-computer")
    cart_page.add_product_to_cart()
    cart_page.open_cart()

    cart_page.should_have_product_in_cart(
        "Build your own cheap computer"
    )

    cart_page.remove_product_from_cart()
    cart_page.should_be_empty()