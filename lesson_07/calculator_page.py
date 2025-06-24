from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.CLASS_NAME, "screen")

    def set_delay(self, delay):
        delay_input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_input_element.clear()
        delay_input_element.send_keys(delay)

    def press_button(self, button_value):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_value}']"))
        )
        button.click()

    def get_result(self):
        # Ждем, пока результат не станет "15"
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(self.result_field, "15")
        )
        return self.driver.find_element(*self.result_field).text
