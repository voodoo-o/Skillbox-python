letter, number = input("Введите букву и цифру через запятую: ").split(',')
number = int(number)

def f(i, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_size = len(alphabet)
    i_index = alphabet.index(i)
    shifted_index = (i_index + n) % alphabet_size
    return alphabet[shifted_index]

print(f(letter, number))
        
