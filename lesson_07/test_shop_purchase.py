import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    yield driver
    driver.quit()


def test_shop_purchase(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    browser.get("https://www.saucedemo.com/")

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        main_page.add_item_to_cart(item)

    main_page.go_to_cart()
    cart_page.verify_items_in_cart(items)
    cart_page.click_checkout()

    checkout_page.fill_form("Имя", "Фамилия", "123456")
    checkout_page.click_continue()

    total = checkout_page.get_total()
    assert total == "Total: $58.29", \
        f"Expected total to be $58.29, but got {total}"
