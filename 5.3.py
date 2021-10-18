import itertools
from itertools import zip_longest, islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'вигшл']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '9А']

rez = (i for i in zip_longest(tutors, klasses)) # создаем кортеж из двух элементов tutors и klasses

#for i in itertools.zip_longest(tutors, klasses):# не генератор
#    print(type(i), i)



print(type(rez))# убедился, что это генератор

print(*islice(rez, 8))# выводим все элементы равные колличеству tutors

print(list(islice(rez, 3)))# доказали истощения генератора
