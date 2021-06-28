class MyOwnError(Exception):
    pass


your_list = []

while True:
    el = input('Введите элемент списка (число) или stop для выхода: ')
    if el == 'stop':
        break
    else:
        try:
            try:
                your_list.append(float(el))
            except ValueError:
                raise MyOwnError()
        except MyOwnError:
            print('Вводите число!!!')
print(your_list)
