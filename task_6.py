password = input('Введите пароль')

while len(password) >= 8 and password.lower() and password.upper():
    print('Допустимый пароль')
    break
else:
    print('Думай ещё')