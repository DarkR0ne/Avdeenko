def f(c, e, flag=True):
    if c == e:
        return flag
    if c == 22:
        flag = False
    if c > e:
        return 0
    if c < e:
        return f(c + 3, e, flag) + f(c + 4, e, flag)


print(f(16, 38))
