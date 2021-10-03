for i in range(0, 101):
    if i % 10 == 1 and i % 100 != 11:
        print(i, 'процент')
    elif 1 < i < 5 and not 11 < i % 100 < 15:
        print(i, 'процента')
    else:
        print(i, 'процентов')






