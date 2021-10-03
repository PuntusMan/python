duration = int(input("введите колличество секунд: "))
if duration < 60:
    print(duration, "сек")
elif duration >= 60 and duration < 3600:
    min = duration // 60
    sec = duration % 60
    print(min,"мин:", sec, "сек")
elif duration >= 3600 and duration < 86400:
    hour = duration // 3600
    min = (duration % 3600) // 60
    sec = duration % 3600 % 60
    print(hour, "час:", min, "мин:", sec, "сек")
else:
    day = duration // 86400
    hour = (duration % 86400) // 3600
    min = ((duration % 86400) % 3600) // 60
    sec = duration % 86400 % 3600 % 60
    print(day,"дней:", hour,"час:", min,"мин:", sec, "сек")
