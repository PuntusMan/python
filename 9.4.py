from random import choice


class Car:
    direction = ["лево", "прямо", "право", "назад"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f"машина: {n} цвет: {c}.\nМашина полиции? {p}")

    def go(self):
        print(f"{self.name}: поехала")

    def stop(self):
        print(f"{self.name}: стоит")

    def turn(self):
        print(f"{self.name}: повернула {choice(self.direction)}")

    def show_speed(self):
        return f"{self.name}: скорость: {self.speed}"


class TownCar(Car):
    def show_speed(self):
        return f"{self.name}: скорость: {self.speed}. превышение" if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}: скорость: {self.speed}. превышение" if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """s"""


class PoliceCar(Car):
    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p=True)


pcar = PoliceCar("полиция", "белый", 90)
wcar = WorkCar("грузовик", "грязный", 45)
scar = SportCar("спорт", "черный", 300)
tcar = TownCar("городская", "красный", 60)

list_car = [pcar, wcar, scar, tcar]
for i in list_car:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()