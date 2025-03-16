def f(x, y):
    return (x + y <= 30) or (y <= x+2) or (y >= a)


for a in range(400):
    if all(f(x, y) == 1 for x in range(0, 500) for y in range(0, 500)):
        print(a)
