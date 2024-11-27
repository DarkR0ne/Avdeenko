a = 15 + 2**10 + 16
b = []
while a > 0:
    b.append(a % 16)
    a //= 16
print(b.count(15))