n = int(input("Введите число n: "))
for i in range(1, n + 1):
    a = [int(j) for j in str(i)]
    b = True
    for digit in a:
        if digit != 0 and i % digit != 0:
            b = False
            break
    if b:
        print(i, end=" ")