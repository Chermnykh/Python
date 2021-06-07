def my_func():
    total = 0
    your_list = input('Введите числа, либо ! для выхода: ').upper().split()
    for i in your_list:
        if i == '!':
            return total, True
        try:
            total += int(i)
        except ValueError:
            pass
    return total, False

result = 0
while True:
    a, b = my_func()
    result += a
    print(result)
    if b:
        break
