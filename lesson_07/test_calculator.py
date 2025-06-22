import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    yield driver
    driver.quit()


def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    page.set_delay("45")
    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    result = page.get_result()
    assert result == "15", "Результат на экране не равен 15"
