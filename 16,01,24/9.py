a = int(input('Введите трёхзначное число '))
b = (a // 100) % 10
c = (a // 10) % 10
d = a % 10
f = b + c
g = c + d
print(f, g, sep="")
