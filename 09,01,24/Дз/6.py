a = int(input('Введите четырёхзначное число '))
b = a // 1000
c = (a // 100) % 10
d = (a // 10) % 10
f = a % 10
print("Тысячи",b)
print("сотни",c)
print("Десятки",d)
print("Единицы",f)