import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page_v2 import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-"
               "webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора: сложение 7 и 8")
@allure.description("Тест проверяет корректность работы "
                    "калькулятора при сложении чисел 7 и 8.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver):
    with allure.step("Открытие страницы калькулятора"):
        page = CalculatorPage(driver)
    with allure.step("Установка задержки 45 секунд"):
        page.set_delay("45")
    with allure.step("Нажатие кнопок: 7, +, 8, ="):
        page.press_button("7")
        page.press_button("+")
        page.press_button("8")
        page.press_button("=")
    with allure.step("Проверка результата"):
        result = page.get_result()
        assert result == "15", "Результат на экране не равен 15"
