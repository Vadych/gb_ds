# Реализовать базовый класс Worker (работник).

# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, 
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: 
# создать экземпляры класса Position, передать данные, 
# проверить значения атрибутов, вызвать методы экземпляров.




class Worker():
    def __init__(self, name, surname, position, wage, bonus) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage, 'bonus': bonus}
        

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'
    
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']
    

test_list = []

test_list.append(Position('Иван', 'Семенов', 'Инженер', 75000, 50000))
test_list.append(Position('Семен', 'Горбунков', 'Слесарь', 60000, 40000))
test_list.append(Position('Ирина', 'Крамер', 'Бухгалтер', 40000, 25000))

for item in test_list:
    print(item.name)
    print(item.surname)
    print(item.position)
    print(item._income)
    print(item.get_full_name())
    print(item.get_total_income())
        

