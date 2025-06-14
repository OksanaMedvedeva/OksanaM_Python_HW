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
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

# Ожидание загрузки каждого из изображений
for i in range(4):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, f"//img[{i+1}]"))
    )

# Получение всех изображений на странице
images = driver.find_elements(By.TAG_NAME, 'img')

# Получение значения атрибута src у 3-й картинки
if len(images) >= 3:
    third_image_src = images[3].get_attribute('src')
    print("Атрибут src третьего изображения:", third_image_src)
else:
    print("На странице меньше трех изображений.")

# Закрытие браузера
driver.quit()
