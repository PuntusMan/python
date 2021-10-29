import os
import django
from collections import defaultdict

def dir_info():
    root_dir = django.__path__[0]  # используем файловую структуру библиотеки django
    django_files = defaultdict(int)
    for root, dict, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))  # длина числа в 10-ой степени его размер, если размер файла 4800, его длина 4, 10^4 = 10 000
            django_files[size] += 1  # сумируется колличество

    for size, nums in sorted(django_files.items()):  # выводит в отсортированом порядке
        print(f"{size}: {nums}")

dir_info()