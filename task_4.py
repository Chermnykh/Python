your_s = input("Введите слова через пробел: ")
words = your_s.split(' ')

for i, word in enumerate(words, 1):
    print(i, word[:10])
