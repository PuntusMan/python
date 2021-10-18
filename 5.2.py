n = int(input('введи число: '))
s = (num for num in range(1, n+1, 2))

print(type(s), *s)# звездочка нужна для распаковки генератора