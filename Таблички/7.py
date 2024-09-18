print(f"x\ty\tz\tw\tf")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x <= (z == w)) or not(y <= w)
                f = int(f)
                if f == 0:
                    print(f"{x}\t{y}\t{z}\t{w}\t{f}")
#zwyx