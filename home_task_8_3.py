# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
# # Параметры нормального распределения
# mean = 0 # Среднее значение
# std_dev = 1 # Стандартное отклонение
# num_samples = 1000 # Количество образцов
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)
# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)

# 1. Создай гистограмму для случайных данных
import numpy as np
import matplotlib.pyplot as plt

# data = np.random.normal(0, 1, 1000)
# plt.hist(data)
#
# plt.xlabel("ось Х")
# plt.ylabel("ось Y")
#
# plt.show()
#
# print(data)


# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`

data2 = np.random.random((2,200))

plt.scatter(data2[0], data2[1])
plt.xlabel("ось Х")
plt.ylabel("ось Y")

plt.show()

print(data2)