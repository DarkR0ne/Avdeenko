def a(a1):
    b = [int(b1) for b1 in str(a1)]
    c = len(b)
    d = sum([b1**c for b1 in b])
    return d == a1
d1 = []
for a1 in range(100,1000):
    if a(a1):
        d1.append(a1)
print("Числа Армстронга: ")
for a1 in d1:
    print(a1)
