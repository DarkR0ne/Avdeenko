def count_ip():
    ips = 2 ** (32 - 15)
    counter = 0
    for i in range(ips):
        bin_counter = bin(i).count("1")
        if bin_counter % 12 == 0:
            counter += 1
    counter2 = ips - counter
    return counter2
result = count_ip()
print(result)

