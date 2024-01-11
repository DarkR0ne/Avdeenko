a,b,c,d,f=map(int, input("Введите пять целых чисел: ").split())
if a>b and a>c and a>d and a>f:
    m=a
elif b>a and b>c and b>d and b>f:
    m=b
elif c>a and c>b and c>d and c>f:
    m=c
elif d>a and d>b and d>c and d>f:
    m=d
elif f>a and f>b and f>c and f>d:
    m=f
print("Максимальное число", m)
