s = int(input("Введите площадь: "))
for i in range(1, int(s**0.5)+1):
    if s % i == 0:
        j = s // i
        print(f"Размеры прямоугольника: {i}x{j}")
