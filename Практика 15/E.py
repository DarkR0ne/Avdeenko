import random
a = [random.randint(1,100) for _ in range(6)]
print("Исходный массив:", a)
revers = len(a) // 2
a[:revers] = a[:revers][::-1]
a[revers:] = a[revers:][::-1]
print("Массив после реверса:", a)