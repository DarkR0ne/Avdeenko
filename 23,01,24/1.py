a = []
for i in range(10000, 100000):
    if i % 133 == 125 and i % 134 == 111:
        a.append(i)
print("Пятизначные числа подходящие под условие задачи: ")
for i in a:
    print(i)