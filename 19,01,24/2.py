a, b = map(int, input("Введите два целых числа: ").split())
b1 = b
a1 = a
c = 0
if (a1 >= 0 and b1 >= 0) or (a1 < 0 and b1 < 0):
    a1 = abs(a1)
    b1 = abs(b1)
    while b1 > 0:
        c += a1
        b1 -= 1
else:
    a1 = abs(a1)
    b1 = abs(b1)
    while b1 > 0:
        c -= a1
        b1 -= 1
print(f"{a} * {b} = {c}")
