import random
a = [random.randint(1, 10) for _ in range(10)]
maximum = max(a)
max_count = a.count(maximum)
print("Массив:", a)
print("Максимальный элемент:", maximum)
print("Количество максимальных элементов:", max_count)