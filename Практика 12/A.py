import random
from typing import List

a, b = [int(i) for i in input().split()]

random_numbers = []
if a >= b:
    print("a должно быть меньше b")
else:
    for _ in range(5):
        random_numbers.append(random.randint(a, b))
        print("Массив cлучайных чисел на отрезке [{},{}]: {}".format(a, b, random_numbers))