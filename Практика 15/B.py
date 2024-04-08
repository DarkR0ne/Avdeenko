import random

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True

random_num = [random.randint(0,100) for _ in range(10)]
prime_num = [num for num in random_num if prime(num)]
print("Первый массив с случайными числами:", random_num)
print("Второй массив с простыми числами:", prime_num)