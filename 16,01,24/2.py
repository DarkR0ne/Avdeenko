a,b,c = [int(i) for i in input("Введите три числа: ").split()]
if a==b and a == c:
    print("Все числа одинаковые")
elif a == b or b == c or a == c:
    print("Два числа одинаковые")
else:
    print("Все числа разные")