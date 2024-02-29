def func(n: int):
    if n <= 36:
        if n % 2 == 0: result = 'Купе верхнее'
        else: result = 'Купе нижнее'
    else:
        if n % 2 == 0: result = 'Боковое верхнее'
        else: result = 'Боковое нижнее'
    return result

while True:
    n = input('Введите номер места: ')
    if n.isdigit() and 0 < int(n) <= 54:
        print(func(int(n)), n)
        break
    else: print('Недопустимое значение')




