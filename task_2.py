with open('text_2.txt', 'r', encoding='UTF-8') as f:
    line = f.readlines()
    for index, value in enumerate(line, 1):
        words = len(value.split())
        print('Строка:', index, 'Слов в строке:', words)
