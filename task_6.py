def int_func(word):
    return word.title()


s = input('Введите слова: ').split()
for i, word in enumerate(s):
    if not word.isalpha() or not word.islower():
        print('Error!')
    else:
        s[i] = int_func(word)

print(' '.join(s))
