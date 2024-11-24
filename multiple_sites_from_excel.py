import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Чтение Excel-файла
excel_file = 'sites_list.xlsx'
df = pd.read_excel(excel_file)

# Поиск столбца с заголовком "адрес"
if 'адрес' in df.columns:
    urls = df['адрес'].dropna().tolist()
else:
    raise ValueError("Столбец 'адрес' не найден в файле.")

# Инициализируйте драйвер
driver = webdriver.Chrome()

try:
    for i, url in enumerate(urls):
        try:
            # Откройте веб-страницу
            driver.get(url)

            # Подождите, пока страница полностью загрузится
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # Сделайте скриншот и сохраните его в файл
            screenshot_path = f'screenshot_{i+1}.png'
            driver.save_screenshot(screenshot_path)
            print(f"Скриншот сохранен: {screenshot_path}")

            # Подождите некоторое время перед переходом к следующему сайту
            time.sleep(2)

        except Exception as e:
            print(f"Ошибка при обработке URL {url}: {e}")

finally:
    # Закройте браузер
    driver.quit()
