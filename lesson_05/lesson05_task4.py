from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = (webdriver.Firefox
          (service=FirefoxService(GeckoDriverManager().install())))

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ввод значения в поле username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Ввод значения в поле password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Задержка для наблюдения результата
sleep(2)

# Нажатие кнопки Login
login_button = driver.find_element(By.CSS_SELECTOR, ".radius")
login_button.click()

# Задержка для наблюдения результата
sleep(2)

# Вывод текста с зеленой плашки в консоль
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
print("Текст с зеленой плашки:", success_message)

# Закрытие браузера
driver.quit()
