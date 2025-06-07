from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = (webdriver.Firefox
          (service=FirefoxService(GeckoDriverManager().install())))

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Поиск поля ввода и ввод текста "Sky"
input_field = (driver.find_element(By.TAG_NAME, "input"))
input_field.send_keys("Sky")

# Задержка для наблюдения результата
sleep(2)

# Очистка поля
input_field.clear()

# Задержка для наблюдения результата
sleep(2)

# Ввод текста "Pro"
input_field.send_keys("Pro")

# Задержка для наблюдения результата
sleep(2)

# Закрытие браузера
driver.quit()
