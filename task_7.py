def fact(n):
    prev = 1
    for i in range(1, n + 1):
        prev = prev * i
        yield prev


n = 5
for el in fact(n):
    print(el)
