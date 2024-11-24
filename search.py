from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Создаем экземпляр браузера (в данном случае Chrome)
driver = webdriver.Chrome()

try:
    # Открываем google.com
    driver.get("https://www.google.com")

    # Находим поле поиска
    search_box = driver.find_element(By.NAME, "q")

    # Вводим запрос от пользователя
    user_query = "захардкоженное значение"  # input("Введите запрос для поиска в Google: ")
    search_box.send_keys(user_query)

    # Отправляем запрос, имитируя нажатие клавиши Enter
    search_box.send_keys(Keys.RETURN)

    # Можно добавить паузу для наблюдения результата
    input("Нажмите Enter, чтобы закрыть браузер...")
finally:
    # Закрываем браузер
    driver.quit()
