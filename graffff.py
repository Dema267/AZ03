import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'
prices = data['Price']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Мы можем изменить количество bin-ов по своему усмотрению

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()

    # Построение гистограммы
    plt.hist(df['Price'], bins=20, color='blue', alpha=0.7, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    if driver:
        driver.quit()