s = input("Введите строку: ")
vowel_letters = "аеёиоуыэюя"
consonant_letters = "бвгджзйклмнпрстфхцчшщъь"
vowel_count = 0
consonant_count = 0

for char in s:
    if char != ' ':
        if char in vowel_letters:
            vowel_count += 1
        elif char in consonant_letters:
            consonant_count +=1
            
print(vowel_count, consonant_count)
            
            
        
