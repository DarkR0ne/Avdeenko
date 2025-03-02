def f(c, e, flag=False, flag1=True, flag2=True):
    if c == 8:
        flag = True
    if c == 11:
        flag1 = False
    if c == 18:
        flag2 = False
    if c == e:
        return flag and flag1 and flag2
    if c > e:
        return 0
    if c < e:
        return f(c + 1, e, flag, flag1, flag2) + f(c + 2, e, flag, flag1, flag2) + f(c * 3, e, flag, flag1, flag2)


print(f(4, 23))
