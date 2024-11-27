print(f"x\ty\tz\tw\tf")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or (not y)) and not(w == z) and (not w)
                f = int(f)
                if f == 1:
                    print(f"{x}\t{y}\t{z}\t{w}\t{f}")
#wyxz