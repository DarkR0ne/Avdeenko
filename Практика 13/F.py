import random
height = [random.randint(120, 180) for _ in range(30)]
team = sum(1 for rost in height if rost > 170)
print(f"Массив роста: {height}")
if team >= 5:
    print(f"Из 30 учеников {team},учеников выше 170 см. Можно сформировать команду из 5 или более человек ")
else:
    print(f"Из 30 учеников {team},учеников выше 170 см. Нельзя сформировать команду из 5 человек ")