list = []
list_2 = []

all_sum = 0

for number in range(0, 1001): # создаем список от 0 до 1000, можно еще так for m in range(1, 1001, 2): интервал нечетных чисел от 1 до 1001
    if number % 2 != 0: # удаляем из списка четные числа
        list.append(number**3 ) # возводим нечетные числа в куб
print('колличество элементов:', len(list)) # проверял колличество элементов
print(list) # проверял список
for n, val in enumerate(list): # enumerate проходит по списку создает к каждому элемнту порядковый номер(индекс)
    n_sum = 0
    while val > 0:
        n_sum = n_sum + val % 10 # убераем последнюю цифру
        val = val // 10# удаляем последнюю цифру
    if n_sum % 7 == 0:
        all_sum = all_sum + list[n]


print(all_sum)

for i in list:
    list_2.append(i + 17)# в первом списке прибовляем 17 к каждому элементу списка

all_sum = 0 #обнуляем переменную all_sum

# копируем блок выше так как действия идентичны

for n, val in enumerate(list_2): # enumerate проходит по списку создает к каждому элемнту порядковый номер(индекс)
    n_sum = 0
    while val > 0:
        n_sum = n_sum + val % 10 # убераем последнюю цифру
        val = val // 10# удаляем последнюю цифру
    if n_sum % 7 == 0:
        all_sum = all_sum + list_2[n]


print(all_sum)




