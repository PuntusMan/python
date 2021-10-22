
# 1 вариант это не сохроняется ни где, а просто выводится на экран
#with open("nginx_logs.txt", "r", encoding="utf-8")as f:
#    c = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)# это генератор
#    for i in c: # выводим построчно
#        print(i)


# 2 вариант
with open("p_logs.txt", "w", encoding="utf-8")as p:# w открываем на запись
    with open("nginx_logs.txt", "r", encoding="utf-8") as f:# открываем на чтение
        c = (f"{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}" for line in f)
        for i in c:
            print(i, file=p)# ничего не выводит на экран, а сразу сохроняет в файл



