def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return max(abs(x2 - x1), abs(y2 - y1))


def center(cluster):
    summ_dit = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        summ_dit.append([sm, p])
    return min(summ_dit)[1]


clusterA = [[], []]
for s in open("27A_18054_2.txt"):
    [x, y] = [float(i) for i in s.split()]
    if y < 5:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

centerA = [center(c) for c in clusterA]
PX = int((sum(x for x, y in centerA) / 2) * 10_000)
PY = int((sum(y for x, y in centerA) / 2) * 10_000)
clusterB = [[], [], []]
for s in open("27B_18054.txt"):
    [x, y] = [float(i) for i in s.split()]
    if x > 3:
        clusterB[0].append([x, y])
    elif y < -2:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(c) for c in clusterB]
PXb = int((sum(x for x, y in centerB) / 3) * 10_000)
PYb = int((sum(y for x, y in centerB) / 3) * 10_000)
print(PX, PY)
print(PXb, PYb)
