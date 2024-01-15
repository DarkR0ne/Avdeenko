import random
a = 0
for i in range(3):
    b = random.randint(1, 6)
    a += b
c = a / 3
print("Общее количество очков:", a)
print("Среднее количество очков:", c)
