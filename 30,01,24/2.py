a = 10
b = 5
c = 0.5
for i in range(11):
    for j in range(21):
        for k in range(201):
            s1 = i*a + j*b + k*c
            s2 = i + j + k
            if (s2<=100) and s1 == 100:
                print(f"быков {i} коров {j} телят {k}")