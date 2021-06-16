with open('text_1.txt', 'w', encoding='UTF-8') as f:
    while True:
        line = input('Введите строку: ')
        if not line:
            break
        f.write(line + '\n')
