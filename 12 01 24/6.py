a = int(input("Возраст Антона: "))
b = int(input("Возраст Бориса: "))
c = int(input("Возраст Виктора: "))
if a>b and a>c:
   print("Антон старше всех")
elif b>a and b>c:
    print("Борис старше всех")
elif c>b and c>a:
    print("Виктор старше всех")
elif a == b and a>c:
    print("Антон и Борис старше Виктора")
elif c == b and c>a:
    print("Борис и Виктор старше Антона")
elif a == c and a>c:
    print("Антон и Виктор старше Бориса")
else:
    print("Они все ровесники")