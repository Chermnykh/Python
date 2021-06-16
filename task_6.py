my_dict = {}
with open('text_6.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        name, rest = line.split(':')
        rest = rest.split()
        num = 0
        for part in rest:
            if "-" in part:
                continue
            nums, type = part.split('(')
            num += int(nums)
        my_dict[name] = num
print(my_dict)
