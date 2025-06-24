from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, ".cart_button").click()

    def get_total(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text
