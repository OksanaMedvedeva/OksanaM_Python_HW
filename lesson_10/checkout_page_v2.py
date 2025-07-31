from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Заполнение формы данными:"
                 " {first_name}, {last_name}, {postal_code}")
    def fill_form(self, first_name, last_name, postal_code):
        """
        Заполняет форму данными пользователя.
        :param first_name: str — имя пользователя.
        :param last_name: str — фамилия пользователя.
        :param postal_code: str — почтовый индекс пользователя.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.step("Нажатие кнопки Continue")
    def click_continue(self):
        """
        Нажимает на кнопку Continue.
        """
        self.driver.find_element(By.CSS_SELECTOR, ".cart_button").click()

    @allure.step("Получение итоговой суммы")
    def get_total(self):
        """
        Возвращает итоговую сумму заказа.
        :return: str — текст итоговой суммы заказа.
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text
