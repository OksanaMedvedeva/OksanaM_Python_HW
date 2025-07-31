from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие кнопки Checkout")
    def click_checkout(self):
        """
        Нажимает на кнопку Checkout.
        """
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("Проверка товаров {items} в корзине")
    def verify_items_in_cart(self, items):
        """
        Проверяет наличие товаров в корзине.
        :param items: list[str] —
        список названий товаров, которые должны быть в корзине.
        """
        for item in items:
            item_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[@class="
                               f"'inventory_item_name' and text()='{item}']")
                )
            )
            assert item_element.is_displayed(), \
                f"Item '{item}' not found in the cart."
