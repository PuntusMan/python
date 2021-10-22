import collections

with open("p_logs.txt", "r", encoding="utf-8") as f:
    d = collections.Counter()#вид словаря, который позволяет нам считать количество неизменяемых объектов (в большинстве случаев, строк)

    for i in f:# перебираем строку за строкой по очереди, экономит память
        i = i.split()[0]
        d[i] +=1

    ip, c = d.most_common(1)[0][0], d.most_common(1)[0][1]#most_common Возвращает список наиболее повторяемых элементов
    print(f"Spamer {ip} -  {c} times")