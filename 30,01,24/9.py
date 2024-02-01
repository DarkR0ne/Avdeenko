n = int(input("Введите число N: "))
a = 0
for i in range(1,n):
    a += len(str(i))
    if a >= n:
        print(f"Александр проехал {i} километров")
        break
