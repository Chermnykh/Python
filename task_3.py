def my_func(a, b, c):
    my_list = [a, b, c]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        print('Введите числа!')


print(my_func(44, 75856, 3))
