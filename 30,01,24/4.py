a, b = map(int, input("Введите границы диапазона: \n").split())
for i in range(a, b+1):
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
        if c > 1:
            break
    if c == 1:
        print(i, end=" ")
