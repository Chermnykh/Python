your_list = []

while True:
    new_el = input("Хотите ввести элемент списка? Y/N ")
    if new_el == "Y":
        new_list = input("Введите элемент списка: ")
        your_list.append(new_list)
    else:
        break

for i in range(1, len(your_list), 2):
    tmp = your_list[i - 1]
    your_list[i - 1] = your_list[i]
    your_list[i] = tmp

print(your_list)
