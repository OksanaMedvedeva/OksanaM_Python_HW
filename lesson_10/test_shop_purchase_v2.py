import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from login_page_v2 import LoginPage
from main_page_v2 import MainPage
from cart_page_v2 import CartPage
from checkout_page_v2 import CheckoutPage


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тестирование покупки в интернет-магазине")
@allure.description("Тест проверяет корректность "
                    "процесса покупки товаров в интернет-магазине.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_purchase(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    with allure.step("Открытие сайта магазина"):
        browser.get("https://www.saucedemo.com/")

    with allure.step("Авторизация пользователя"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    with allure.step("Добавление товаров в корзину"):
        for item in items:
            main_page.add_item_to_cart(item)

    with allure.step("Переход в корзину"):
        main_page.go_to_cart()

    with allure.step("Проверка товаров в корзине"):
        cart_page.verify_items_in_cart(items)

    with allure.step("Нажатие кнопки Checkout"):
        cart_page.click_checkout()

    with allure.step("Заполнение формы данными пользователя"):
        checkout_page.fill_form(
            "Имя", "Фамилия", "123456"
        )

    with allure.step("Нажатие кнопки Continue"):
        checkout_page.click_continue()

    with (allure.step("Проверка итоговой суммы")):
        total = checkout_page.get_total()
        assert total == "Total: $58.29", ("Expected total "
                                          "to be $58.29, but got {total}")
