a, b = map(int, input("Введите границы диапазона: \n").split())
for i in range(a, b+1):
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c += 1
        if c > 2:
            break

    if c == 2:
        print(i, end=" ")
