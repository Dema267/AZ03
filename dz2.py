import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 50  # Количество точек
x = np.random.rand(num_points)  # Первый набор случайных данных (ось X)
y = np.random.rand(num_points)  # Второй набор случайных данных (ось Y)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='blue', alpha=0.7, edgecolor='black')

# Добавление заголовка и подписей осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Отображение графика
plt.show()