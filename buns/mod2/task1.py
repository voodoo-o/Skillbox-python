a, b = input("Введите два числа через запятую: ").split(',')
a = int(a)
b = int(b)

if b == 0:
    print('На ноль делить нельзя')
else:
    c = a % b
    print(c)
