def DEL(x, a):
    return (x % 33 == 0) <= ((not(x % a == 0)) <= (not(x % 242 == 0)))


for a in range(1, 10000):
    if all(DEL(x, a) == 1 for x in range(1, 10000)):
        print(a)
#726