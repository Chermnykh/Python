def div (a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!!!')
    except ValueError:
        print('Введите целое число')


print(div(input('Введите первое число: '), input('Введите второе число: ')))
