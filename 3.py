def func(n: int):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return f'Год {n} - високосный'
    return 'Этот год не високосный'

while True:
    n = input('Введите год: ')
    if n.isdigit():
        print(func(int(n)))
        break
    else: print('Недопустимое значение')

