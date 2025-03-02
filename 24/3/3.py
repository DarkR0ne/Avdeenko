s = open("3").readline()
print(s[:100])
m = [0] * len(s)
for i in range(len(s)):
    if s[i] in "0123456789":
        m[i] = m[i-1]+1
print(max(m))

