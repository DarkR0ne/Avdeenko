a,b,c=map(int, input("Введите три целых числа: ").split())
if a>b and a>c:
    m=a
elif b>a and b>c:
    m=b
elif c>a and c>b:
    m=c
print("Максимальное число", m)

