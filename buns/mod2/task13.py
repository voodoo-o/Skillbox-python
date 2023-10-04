barcode = input("Введите штрих-код: ")
odd_sum = 0
even_sum = 0
position = 1

for i in barcode:
    if position % 2 == 0:
        even_sum += int(i) * 3
    else:
        odd_sum += int(i)
    position += 1
    
if (odd_sum + even_sum) % 10 == 0:
    print("yes")
else:
    print("no")
