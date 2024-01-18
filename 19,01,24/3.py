def i(n):
    c = 0
    a, b = 0, 1
    while b < n:
        c += b
        a, b = b, a + b
    return c
N = int(input("Введите число N: \n"))
f = i(N)
if N > 0:
    print(f"Сумма всех чисел Фибоначчи до числа N {f}")
else:
    print("Введено отрицательное число, повторите ввод")
