def prime_factors(n, divisor=2):
    factors = []
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    if n > 1:
        factors.append(n)
    return factors


def prime_factors2(number):
    factors = prime_factors(number)
    factors_str = "*".join(str(factor) for factor in factors)
    return f"{number} = {factors_str}"


num = int(input("Введите натуральное число: \n"))
result = prime_factors2(num)
print(result)
