with open(input("Введите имя файла: "), encoding="utf-8") as file:
    letters = [symbol for symbol in file.read() if symbol.isalpha()]

letters_count = {letter: letters.count(letter) for letter in set(letters)}
letters_count_sorted = sorted(letters_count.items(), key=lambda item: item[1])
lines = [f"Буква {letter} встречается {count} раз(а)." for letter, count in letters_count_sorted]

with open(input("Введите имя нового файла: "), "w", encoding="utf-8") as file:
    file.write("\n".join(lines))
