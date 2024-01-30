a = 15
b = 17
c = 21
for i in range(13):
    for j in range(11):
        for k in range(9):
            s = i*a + j*b + k*c
            s1 = i + j + k
            if (s1<=185) and s == 185:
                print(f" Ящиков по 15 кг: {i}, ящиков по 17 кг: {j}, ящиков по 21 кг: {k}.")
