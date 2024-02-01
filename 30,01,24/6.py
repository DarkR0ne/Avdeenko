m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
for i in range(1, n):
    a = sum(int(digit) for digit in str(i))
    if i == (m+m)**2:
        print(i)