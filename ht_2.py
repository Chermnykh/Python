class MyOwnError(Exception):
    pass


try:
    try:
        divisible = int(input('Введите делимое: '))
        divisor = int(input('Введите делитель: '))
        res = divisible / divisor
    except ZeroDivisionError:
        raise MyOwnError()
    else:
        print('Результат деления: ', round(res, 2))
except MyOwnError:
    print("Делить на ноль нельзя!")
finally:
    print('Все)')
