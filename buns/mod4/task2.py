def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a ** 2, n // 2)
    else:
        return a * power(a, n - 1)


base, exponent = map(int, input("Введите число и степень через пробел: ").split())
print(f"{base} ^ {exponent} = {power(base, exponent)}")
