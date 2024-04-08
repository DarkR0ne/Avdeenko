import random
a = [random.randint(-100,100) for _ in range(10)]
print("Исходный массив:", a)
a.sort(key=lambda x: x < 0)
count_pos = sum(1 for num in a if num >= 0)
print("Массив после перестановки:", a)
print("Количество положительных элементов:", count_pos)