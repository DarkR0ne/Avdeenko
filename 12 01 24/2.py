import random
a = []
for _ in range(3):
    b = random.randint(1, 6)
    a.append(str(b))
c = int("".join(a))
d = c ** 2
print("Составленное число:", c)
print("Квадрат составленного числа:", d)
