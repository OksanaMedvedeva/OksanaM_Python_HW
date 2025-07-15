from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.CLASS_NAME, "screen")

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param delay: int — время задержки в секундах.
        """
        delay_input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_input_element.clear()
        delay_input_element.send_keys(delay)

    @allure.step("Нажатие кнопки '{button_value}'")
    def press_button(self, button_value):
        """
        Нажимает на кнопку калькулятора.
        :param button_value: str — текст на кнопке, которую нужно нажать.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_value}']"))
        )
        button.click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.
        :return: str — текст результата на экране калькулятора.
        """
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(self.result_field, "15")
        )
        return self.driver.find_element(*self.result_field).text
