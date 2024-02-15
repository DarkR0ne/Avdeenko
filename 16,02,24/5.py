def div(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a1,b1 = map(int, input("Введите два натуральных числа: \n").split())
N = div(a1, b1)
print(f"НОД ({a1},{b1}) = {N}.")
