from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Переход на страницу
driver.get("http://uitestingplayground.com/textinput")

# Ввод текста в поле ввода
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Нажатие на синюю кнопку
button = driver.find_element(By.ID, "updatingButton")
button.click()

# Ожидание обновления текста кнопки и получение текста
updated_button_text = WebDriverWait(driver, 3).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

# Получение и вывод текста кнопки
button_text = driver.find_element(By.ID, "updatingButton").text
print(button_text)

# Закрытие браузера
driver.quit()
