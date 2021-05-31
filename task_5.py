my_list = [7, 5, 3, 3, 2]
n = int(input('Введите число: '))

def add_struct(struct_l, n):
    for ind, el in enumerate(struct_l):
        if n > el:
            struct_l.insert(ind, n)
            return struct_l
    struct_l.append(n)
    return struct_l

print(add_struct(my_list, n))
