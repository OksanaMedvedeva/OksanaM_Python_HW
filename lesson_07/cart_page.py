from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def verify_items_in_cart(self, items):
        for item in items:
            item_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[@class='inventory_item_name' "
                               f"and text()='{item}']")
                )
            )
            assert item_element.is_displayed(), \
                f"Item '{item}' not found in the cart."
