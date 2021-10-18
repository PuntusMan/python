src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([i for i in src if src.count(i)==1])


'''r = []
for i in src:
    if src.count(i) == 1:
        r.append(i)
print(r)'''


my_dict = {i: 0 for i in src}# создаем словарь где ключ = элементам src, ключи не повторяются, а каждое значение ключа это 0

print(type(my_dict))
print(my_dict)

for i in src:
    my_dict[i] +=1
print(my_dict)

print([i for i in my_dict if my_dict[i] == 1])#выводим числа которые не повторяются