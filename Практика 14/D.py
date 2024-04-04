import random
a = [random.randint(1, 100) for _ in range(10)]
minimum = min(a)
min_index = a.index(minimum)
maximum = max(a)
max_index = a.index(maximum)
print("Массив: ", a)
print("Минимальный элемент: ", minimum, f"[{min_index}]")
print("Максимальный элемент: ", maximum,f"[{max_index}]")