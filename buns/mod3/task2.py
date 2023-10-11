n = int(input())
print(bin(n)[2:],oct(n)[2:],hex(n)[2:].upper()) if n>=0 else print("Неверный ввод")
