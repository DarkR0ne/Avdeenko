def f(x, y):
    return (2 * y + x != 70) or (x < y) or (a < x)


for a in range(400):
    if all(f(x, y) == 1 for x in range(0, 500) for y in range(0, 500)):
        print(a)
