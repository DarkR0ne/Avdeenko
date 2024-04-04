import random
a = [random.randint(1, 10) for _ in range(10)]
dubl = False
for i in range(len(a)):
    for i in range(i+1, len(a)):
        if a[i] == a[i]:
            dubl = True
            break
    if dubl:
        break


if dubl:
    print("Массив:", a)
    print("Да")
else:
    print("Массив:", a)
    print("Нет")