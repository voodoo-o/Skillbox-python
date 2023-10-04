words = input("Напишите слова через пробел: ")
result = ""
current_word = ""

for char in words:
    if char != " ":
        current_word += char
    else:
        if current_word:
            result += current_word[-1]
        current_word = ""
        
if current_word:
    result += current_word[-1]

print(result)
