def is_armstrong_number(number):
    number_string = str(number)
    number_power = len(number_string)
    number_sum = 0
    for digit in number_string:
        number_sum += int(digit) ** number_power
    return number_sum == number


def get_armstrong_numbers():
    global current_number
    while True:
        if is_armstrong_number(current_number):
            result = current_number
            current_number += 1
            return result
        current_number += 1


current_number = 10
for i in range(8):
    print(get_armstrong_numbers(), end=' ')
