import random
n = int(input("Введите кол-во элементов в массиве: "))
a = [random.randint(1, 100) for _ in range(n)]
sum_a = n * (n+1) // 2
print(f"Массив: {a}")
print(f"Закономерная сумма элементов массива A равна: {sum_a}")