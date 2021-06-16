numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('text_4.txt', 'r', encoding='UTF-8') as f:
    with open('text_4_1.txt', 'w', encoding='UTF-8') as f2:
        for line in f:
            en, _, num = line.split()
            ru = numbers[en]
            f2.write(' '.join([ru] + [num]) + '\n')
