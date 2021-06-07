def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Введите действительное х и целое у')
        return
    if x <= 0 or y >= 0:
        print('Введите положительное х и отрицательное у')
        return
    return x**y


print(my_func(4, -1))
