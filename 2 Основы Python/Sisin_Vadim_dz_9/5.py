# Реализовать класс Stationery (канцелярская принадлежность).

# определить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. 
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, name):
        self.name = name
    
    def draw(self):
        print (f'{self.name} не умеет рисовать')
        

class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.name} рисует черильную полосу')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.name} оставляет след грифеля')      
        

class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.name} выделяет строку в тексте')
        
test_list = []
test_list.append(Stationery('Чебурашка'))
test_list.append(Pen('Parker'))
test_list.append(Pencil('Мягкий'))
test_list.append(Handle('Желтый'))

for item in test_list:
    item.draw()