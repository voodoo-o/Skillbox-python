phone = input("Введите номер телефона: ")
cleaned_phone = ""
chars = "0123456789+"

for i in phone:
    if i in chars:
        cleaned_phone += i

print(cleaned_phone)

