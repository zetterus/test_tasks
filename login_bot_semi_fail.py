from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import time

# Путь к исполняемому файлу Tesseract (замени путь, если другой)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Данные для входа
login = "zettec"
password = "iay8gB5rKktkSH!"

# Создаем экземпляр браузера
driver = webdriver.Chrome()

try:
    print("Открываем сайт LostFilm...")
    driver.get("https://www.lostfilm.tv")
    print("Сайт успешно открыт.")

    # Нажимаем на кнопку "Вход"
    try:
        print("Ищем кнопку 'Вход'...")
        login_button = driver.find_element(By.XPATH, '//*[@id="main-rightt-side"]/div[1]/a[1]')
        login_button.click()
        print("Кнопка 'Вход' нажата.")
        time.sleep(2)  # Ждем загрузки окна входа
    except Exception as e:
        print(f"Ошибка при поиске или нажатии на кнопку 'Вход': {e}")
        driver.quit()
        exit()

    # Находим контейнер с формой входа
    try:
        print("Ищем контейнер с формой входа...")
        login_container = driver.find_element(By.ID, "left-pane")
        print("Контейнер найден.")
    except Exception as e:
        print(f"Ошибка при поиске контейнера формы входа: {e}")
        driver.quit()
        exit()

    # Ввод логина
    try:
        print("Ищем поле для ввода логина внутри контейнера...")
        login_field = login_container.find_element(By.XPATH, '//*[@id="left-pane"]/div[3]/div/div[5]/input')
        login_field.send_keys(login)
        print("Логин успешно введен.")
    except Exception as e:
        print(f"Ошибка при вводе логина: {e}")
        driver.quit()
        exit()

    # Ввод пароля
    try:
        print("Ищем поле для ввода пароля внутри контейнера...")
        password_field = login_container.find_element(By.XPATH, '//*[@id="left-pane"]/div[3]/div/div[7]/input')
        password_field.send_keys(password)
        print("Пароль успешно введен.")
    except Exception as e:
        print(f"Ошибка при вводе пароля: {e}")
        driver.quit()
        exit()

    try:
        print("Проверяем, присутствует ли капча на странице...")
        # Ждем, пока элемент капчи станет видимым (максимум 5 секунд)
        captcha_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="left-pane"]/div[3]/div/div[8]/div[3]'))
        )

        if captcha_element.is_displayed():
            # Если капча найдена и видна, сохраняем её изображение и вводим текст
            print("Капча обнаружена, сохраняем изображение и распознаем текст.")
            captcha_element.screenshot("captcha.png")  # Сохраняем капчу
            captcha_text = pytesseract.image_to_string(Image.open("captcha.png"), config="--psm 6").strip()
            print(f"Распознанная капча: {captcha_text}")

            # Вводим капчу в поле
            captcha_field = login_container.find_element(By.CLASS_NAME, "text-input")
            captcha_field.send_keys(captcha_text)
            print("Капча успешно введена.")
        else:
            print("Капча не найдена.")
    except Exception as e:
        print(f"Ошибка при проверке и вводе капчи: {e}")

    # Нажимаем кнопку "ВОЙТИ"
    try:
        print("Ищем кнопку 'ВОЙТИ' внутри контейнера...")
        submit_button = login_container.find_element(By.CLASS_NAME, "primary-btn")
        submit_button.click()
        print("Кнопка 'ВОЙТИ' нажата.")
        time.sleep(3)  # Ждем загрузки страницы после входа
    except Exception as e:
        print(f"Ошибка при нажатии кнопки 'ВОЙТИ': {e}")
        driver.quit()
        exit()

    # Находим строку поиска
    try:
        print("Ищем строку поиска...")
        search_field = driver.find_element(By.NAME, "q")
        search_field.send_keys("светлячок")
        search_field.send_keys(Keys.RETURN)  # Имитируем нажатие Enter
        print("Поисковый запрос 'светлячок' успешно отправлен.")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")
        driver.quit()
        exit()

    input("Нажмите Enter, чтобы закрыть браузер...")
finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт.")
