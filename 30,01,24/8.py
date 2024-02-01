for i in range(1, 10000):
    a = 0
    b = 0
    for j in range(1, i):
        if i % j == 0:
            a += j
    for k in range(1, a):
        if a % k == 0:
            b += k
    if i == b and i < a:
        print(i, a)