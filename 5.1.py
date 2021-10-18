def gen (n):
    for n in range(1, n+1, 2): # создаем список нечетных чисел
        yield n

for i in gen(10):
    print(i, type(i))