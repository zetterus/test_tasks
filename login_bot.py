from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализируйте драйвер
driver = webdriver.Chrome()

try:
    # Откройте страницу входа
    driver.get("https://combats.com/")

    # Найдите поля ввода для логина и пароля и введите данные
    login_field = driver.find_element(By.NAME, "login")
    password_field = driver.find_element(By.NAME, "psw")

    login_field.send_keys("zettec")
    password_field.send_keys("iay8gB5rKktkSH!")

    # Найдите кнопку входа и нажмите её
    login_button = driver.find_element(By.NAME, "enter_btn")
    login_button.click()

    # Подождите некоторое время, чтобы убедиться, что вход выполнен
    time.sleep(5)

finally:
    # Закройте браузер
    driver.quit()
