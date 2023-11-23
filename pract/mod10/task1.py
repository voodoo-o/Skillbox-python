import re


def is_valid_password(password):
    regex = r"^(?=.*[A-Z].*[A-Z])(?=.*\d)(?=.*[$^%@#&*!?])(?!.*(.)\1{2})[A-Za-z0-9$^%@#&*!?-]{6,}$"
    return re.match(regex, password) is not None


passwords = [
    'rtG3FG!Tr^e',
    'aA1!*!1Aa',
    'oF^a1D@y5e6',
    'enroi#$rkdeR#$092uWedchf34tguv394h',
    'пароль',
    'password',
    'qwerty',
    'lOngPa$$$W0Rd'
]

for password in passwords:
    print(f'{password} - {is_valid_password(password)}')
