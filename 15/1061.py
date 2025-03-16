def f(x, y):
    return (2 * x + 3 * y != 72) or ((a > x) and (a > y))


for a in range(400):
    if all(f(x, y) == 1 for x in range(0, 500) for y in range(0, 500)):
        print(a)
