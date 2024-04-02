import random
mass_p = [random.randint(60, 140) for _ in range(25)]
fat = []
norm = []
for mass in mass_p:
    if mass > 100:
        fat.append(mass)
    else:
        norm.append(mass)
avr_mass_fat = sum(fat) / len(fat)
avr_mass_norm = sum(norm) / len(norm)
print("Средняя масса полных людей: ", avr_mass_fat)
print("Средняя масса остальных людей: ", avr_mass_norm)