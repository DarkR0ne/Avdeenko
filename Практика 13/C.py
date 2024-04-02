import random
import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        return True


arr = [random.randint(2, 100) for _ in range(10)]
pr_num = [num for num in arr if is_prime(num)]
avr = sum(pr_num) / len(pr_num) if pr_num else 0

print(f"Массив случаных чисел: {arr}")
print(f"Простые числа в масииве: {pr_num}")
print(f"Среднее значение простых чисел: {avr}")
