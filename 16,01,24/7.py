a = int(input("Введите количество отработанных часов: "))
b = int(input("Введите траты на одежду: "))
c = int(input("Введите траты на еду: "))
d = (250*a)/2**3 + a
if a > b+c:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать больше!")