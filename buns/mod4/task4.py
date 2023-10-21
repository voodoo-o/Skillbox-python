def can_make_palindrome(word):
    letter_count = {letter: word.count(letter) for letter in set(word)}
    odds = [x for x in letter_count.values() if x % 2 != 0]
    return len(odds) <= 1


def make_palindrome(word):
    letter_count = {letter: word.count(letter) for letter in set(word)}
    left_half, odd_char = "", ""
    for letter, count in letter_count.items():
        if count % 2 != 0:
            odd_char = letter
        left_half += letter * (count // 2)
    return left_half + odd_char + left_half[::-1]


some_word = input("Введите слово: ")
if can_make_palindrome(some_word):
    palindrome = make_palindrome(some_word)
    print(f"Из слова '{some_word}' можно составить палиндром: {palindrome}")
else:
    print(f"Из слова '{some_word}' нельзя составить палиндром.")
