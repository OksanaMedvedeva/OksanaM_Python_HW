from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture(scope="module")
def browser():
    # Автоматическая установка и настройка драйвера Edge
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
    )
    yield driver
    driver.quit()


def test_form_submission(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Ожидание загрузки страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='first-name']"))
    )

    # Заполнение формы
    first_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='first-name']"))
    )
    first_name.send_keys("Иван")

    last_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='last-name']"))
    )
    last_name.send_keys("Петров")

    address = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='address']"))
    )
    address.send_keys("Ленина, 55-3")

    email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='e-mail']"))
    )
    email.send_keys("test@skypro.com")

    phone = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='phone']"))
    )
    phone.send_keys("+7985899998787")

    city = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='city']"))
    )
    city.send_keys("Москва")

    country = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='country']"))
    )
    country.send_keys("Россия")

    job_position = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='job-position']"))
    )
    job_position.send_keys("QA")

    company = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='company']"))
    )
    company.send_keys("SkyPro")

    # Отправка формы
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # Ожидание обновления страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, "zip-code"))
    )

    # Проверка подсветки полей
    zip_code_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".alert.py-2.alert-danger"))
    )
    assert "danger" in zip_code_field.get_attribute("class")

    other_fields = browser.find_elements(
        By.CSS_SELECTOR, ".alert.py-2.alert-success")
    # Проверка, что остальные поля подсвечены зеленым
    assert len(other_fields) == 9
