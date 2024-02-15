def inv(n):
    inv_num = 0
    while n > 0:
        last_num = n % 10
        inv_num = inv_num * 10 + last_num
        n //= 10
    return inv_num


a = int(input("Введите натуральное число: \n"))
inv_num = inv(a)
print("После переворота: ",inv_num)