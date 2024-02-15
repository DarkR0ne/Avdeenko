def sum_num(n):
    sum0 = 0
    while n > 0:
        sum0 += n % 10
        n //= 10
    return sum0


a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
sum1 = sum_num(a)
sum2 = sum_num(b)
if sum1 > sum2:
    print(f"Сумма цифр числа {a} больше, чем сумма цифр числа {b}.")
elif sum1 < sum2:
    print(f"Сумма цифр числа {b} больше, чем сумма цифр числа {a}.")
else:
    print(f"Сумма цифр чисел {a} и {b} равна.")
