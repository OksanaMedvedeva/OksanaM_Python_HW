from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(scope="module")
def browser():
    # Автоматическая установка и настройка драйвера FireFox
    driver = (
        webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    )
    yield driver
    driver.quit()


def test_shop_purchase(browser):
    # Открытие сайта
    browser.get("https://www.saucedemo.com/")

    # Авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item in items:
        item_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((
                By.XPATH, f"//div[text()='{item}']"
                          f"/ancestor::div[@class='inventory_item']//button"
            ))
        )
        item_element.click()

    # Переход в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажатие кнопки Checkout
    browser.find_element(By.ID, "checkout").click()

    # Заполнение формы
    browser.find_element(By.ID, "first-name").send_keys("Имя")
    browser.find_element(By.ID, "last-name").send_keys("Фамилия")
    browser.find_element(By.ID, "postal-code").send_keys("123456")
    browser.find_element(By.CSS_SELECTOR, ".cart_button").click()

    # Чтение итоговой стоимости
    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total = total_element.text

    # Проверка итоговой суммы
    assert total == "Total: $58.29", \
        f"Expected total to be $58.29, but got {total}"
