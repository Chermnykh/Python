with open('text_5.txt', 'w', encoding='UTF-8') as f:
    f.write(input('Введите числа через пробел: '))

with open('text_5.txt', 'r', encoding='UTF-8') as f:
    numbers = [int(i) for i in f.read().split()]
    print("Сумма введенных чисел:", sum(numbers))
