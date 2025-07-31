from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление товара '{item_name}' в корзину")
    def add_item_to_cart(self, item_name):
        """
        Добавляет товар в корзину.
        :param item_name: str — название товара.
        """
        item_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[text()='{item_name}']"
                           f"/ancestor::div[@class='inventory_item']//button")
            )
        )
        item_element.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переходит в корзину.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
