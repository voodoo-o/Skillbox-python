list_ = input("Введите числа через пробел: ").split()
set_ = set(list_)

if len(set_) == 1:
    print("Все числа равны")
elif len(set_) == len(list_):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")

