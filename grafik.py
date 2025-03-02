from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Укажите путь к geckodriver
service = Service('путь/к/geckodriver')
driver = webdriver.Firefox()

# URL страницы
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'

# Открытие страницы
driver.get(url)

# Ожидание появления элементов
try:
    wait = WebDriverWait(driver, 10)  # Ждем до 10 секунд
    prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@data-mark='MainPrice']/span")))

    # Открытие CSV файла для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовок столбца

        # Записываем цены в CSV файл
        for price in prices:
            writer.writerow([price.text])

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()