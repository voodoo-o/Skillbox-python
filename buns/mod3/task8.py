phone = input("Введите номер телефона: ")
cleaned_phone = ''.join(char for char in phone_input if char.isdigit() or char == '+')
print(cleaned_phone)
