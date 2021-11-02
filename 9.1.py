from time import sleep #sleep() позволяет отсрочить выполнение вызываемого потока на указанное количество секунд.

class TrafficLight:    # создали класс
    __color = "цвет"  # создали атрибут
    def running(self): # создали метод
        while True:
            print('красный')
            sleep(7)
            print('желтый')
            sleep(2)
            print('зеленый')
            sleep(3)
            break

t = TrafficLight()
t.running()

