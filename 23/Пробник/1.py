def f(c, e):
    if c < e or c == 16:
        return 0
    if c == e:
        return 1
    if c > e:
        return f(c - 2, e) + f(c / 3, e)
    else:
        return f(c - 2, e) + f(c - 4, e)


print(f(36, 4))
