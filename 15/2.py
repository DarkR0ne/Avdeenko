def DEL(x, a):
    return ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)


for a in range(1, 10000):
    if all(DEL(x, a) == 1 for x in range(1, 10000)):
        print(a)
#1260