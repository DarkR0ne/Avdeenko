s = open("1").readline()
l = 0
m = 0
for r in range(len(s)):
    if s[r] in "CD":
        l = r + 1
    if s[r] in "ABEF":
        m = max(m, r - l + 1)
print(m)