def a1(a):
    sq = a ** 2
    sq_str = str(sq)
    a_str = str(a)
    return sq_str.endswith(a_str)


n = int(input("Введите число N: "))
aut_num = []
for a in range(n+1):
    if a1(a):
        aut_num.append(a)
print("Автоморфные числа:")
for a in aut_num:
    print(f"{a} * {a} = {a**2}")

