from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ввод имени пользователя: {username}")
    def enter_username(self, username):
        """
        Вводит имя пользователя в поле ввода.
        :param username: str — имя пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        """
        Вводит пароль в поле ввода.
        :param password: str — пароль пользователя.
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Нажатие кнопки Login")
    def click_login(self):
        """
        Нажимает на кнопку Login.
        """
        self.driver.find_element(By.ID, "login-button").click()
