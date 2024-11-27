from itertools import count

a = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 5 * 25**4 - 2025
b = []
while a > 0:
    b.append(a % 25)
    a //= 25
print(b.count(0))