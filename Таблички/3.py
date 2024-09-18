print(f"w\tx\ty\tz\tf")
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = ((w <= y) <= x) or (not z)
                f = int(f)
                if f == 0:
                    print(f"{w}\t{x}\t{y}\t{z}\t{f}")
#zwyx