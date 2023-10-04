s = input("Введите последовательность цифр: ")

def f(s):
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                return True
            j += 1
        i += 1
    return False

print(f(s))
