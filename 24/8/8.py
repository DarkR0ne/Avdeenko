s = open("8").readline()
s = s.replace("A", "4"). replace("0", "4").replace("B", "0").replace("C", "0").replace("D", "0")
s = s.replace("01", "B").replace("4", "0").replace("0", " ").split
print(max(len(i) for i in s))