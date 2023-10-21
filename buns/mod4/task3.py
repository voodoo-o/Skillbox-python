def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


num1, num2 = map(int, input("Введите числа через пробел: ").split())
print(euclid(num1, num2))
