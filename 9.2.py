

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def f(self, w=25, t=5):
        return f"{self._width} м * {self._lenght} м {w} кг * {t} см =" \
        f"{int((self._lenght * self._width * w * t)/1000)} т"

a = Road(5000, 20)
print(a.f())