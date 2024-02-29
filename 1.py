def register():
    password = input('Введите пароль: ')
    confirmPassword = input('Подвердите пароль: ')
    return [password, confirmPassword]

while True:
    password, conPassword = register()
    if password == conPassword:
        print('Пароль принят')
        break
    else: print('Пароль не принят, попробуйте снова.')
