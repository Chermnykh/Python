def new_item():
    item_number = input('укажите номер товара: ')
    name = input('укажите название товара: ')
    price = int(input('укажите цену товара: '))
    count_i = int(input('укажите количество товара: '))
    mesure = input('укажите ед товара: ')
    return (item_number, {"название": name, "цена": price, "количество": count_i, "eд": mesure})

items = []
while True:
    new_item_check = input('Хотите задать товар? (Y/N) ')
    if new_item_check == 'Y':
        item = new_item()
        items.append(item)
    else:
        break

analythic = {}
for i in items:
    for y in i[1].keys():
        if y in analythic.keys():
            analythic[y].add(i[1][y])
        else:
            analythic[y] = set()
            analythic[y].add(i[1][y])
analythic = {x: list(analythic[x]) for x in analythic}

for key, value in analythic.items():
    print("{0}: {1}".format(key,value))
