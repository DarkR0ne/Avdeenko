import random
a = random.randint(100, 999)
a1 = a // 100
a2 = (a // 10) % 10
a3 = a % 10
print("Цифры числа ",a)
print(f"Цифры числа через запятую {a1},{a2},{a3}")