import os

p_list = {"my_project": [{"settings": []}, {"mainapp": []}, {"adminapp": []}, {"authapp": []}]}  # создали словарь

for k, v in p_list.items():  # items используетя для перебора словаря
    if not os.path.exists(k):  # os.path.exists - возвращает True, если path указывает на существующий путь
        for item in v:
            for i in item.keys():  # keys() - возвращает ключи в словаре
                os.makedirs(os.path.join(k, i))  # makedirs создает несколько папок
