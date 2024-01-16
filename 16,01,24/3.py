a = int(input("Введите номер месяца: "))
if a >= 1 and a <= 2 or a == 12:
    print("Зима.")
elif a>=3 and a<=5:
    print("Весна.")
elif a>= 6 and a <=8:
    print("Лето.")
elif a > 8 and a < 13 and a != 12:
    print("Осень.")
else:
    print("Неверный номер месяца.")