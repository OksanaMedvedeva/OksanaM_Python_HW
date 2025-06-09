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
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
button.click()

# Ожидание появления зеленой плашки и получение текста
green_panel = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)
text = green_panel.text

# Вывод текста в консоль
print(text)

# Закрытие браузера
driver.quit()
