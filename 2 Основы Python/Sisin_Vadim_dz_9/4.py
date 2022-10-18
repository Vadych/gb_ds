# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость 
# автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться 
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

from distutils import dir_util


class Car:
    def __init__(self, name, color) -> None:
        self.speed = 0
        self.name = name
        self.color = color
        self.is_police = False
        self._add_speed = 20
        self._div_speed = 30
        self.direction = 'прямо'
    
    def go(self):
        self.speed += self._add_speed
        
    def stop(self):
        self.speed -= self._div_speed
        if self.speed < 0:
            self.speed = 0
    
    def turn(self, direction):
        self.direction = direction.lower()
        print('Направление - ', self.direction)
        
    def show_speed(self):
        print ('Скорость - ', self.speed)
    

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('!!!Скорость превышена!!!', self.speed)
        else:
            super().show_speed()

    
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('!!!Скорость превышена!!!', self.speed)
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._add_speed = 30
        self._div_speed = 40

class PoliceCar(Car):
    def __init__(self, name, color) -> None:
        super().__init__(name, color)
        self.is_police = True
        

test_list = []
test_list.append(TownCar('Автобус', 'Красный'))
test_list.append(WorkCar('Газель', 'Белая'))
test_list.append(SportCar('Порше', 'Красный'))
test_list.append(PoliceCar('ГИБДД', 'Синий'))

for car in test_list:
    print(f'{car.color} {car.name}')
    car.go()
    car.go()
    car.go()
    car.go()
    car.show_speed()
    car.stop()
    car.show_speed()
    car.turn('Влево')