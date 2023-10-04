s, i = input("Введите строку и символ через запятую: ").split()
count = 0

for char in s:
    if char == i:
        count +=1
    else:
        print(count)
        break
    
