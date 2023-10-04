a = int(input("Введите число: "))

if a <= 0:
    print('Неверный ввод')
else:
    def res_2(a):
        result_2 = ''
        
        while a > 0:
            remainder_2 = a % 2
            result_2 = str(remainder_2) + result_2
            a //= 2
        return result_2

    def res_8(a):
        result_8 = ''
        
        while a > 0:
            remainder_8 = a % 8
            result_8 = str(remainder_8) + result_8
            a //= 8 
        return result_8

    def res_16(a):
        characters = "0123456789ABCDEF"
        result_16 = ""
        
        while a > 0:
            remainder_16 = a % 16
            result_16 = characters[remainder_16] + result_16
            a //= 16
        return result_16
        
print(res_2(a), res_8(a), res_16(a))
