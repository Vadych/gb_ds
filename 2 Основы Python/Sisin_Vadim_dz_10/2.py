from abc import ABC, abstractproperty


class Clothes(ABC):
    def __init__(self, name_model):
        self.__name_model = name_model

    def __str__(self):
        return self.type_clothes + ' модели ' + self.name_model

    @property
    def name_model(self):
        return self.__name_model

    @abstractproperty
    def fabric_quantity(self):
        pass

    @abstractproperty
    def type_clothes(self):
        pass


class Coat(Clothes):
    def __init__(self, name_model, size):
        super().__init__(name_model)
        self.size = size

    @property
    def fabric_quantity(self):
        return self.size / 6.5 + 0.5

    @property
    def type_clothes(self):
        return 'Пальто'


class Suit(Clothes):
    def __init__(self, name_model, height):
        super().__init__(name_model)
        self.height = height

    @property
    def fabric_quantity(self):
        return self.height * 2 + 0.3

    @property
    def type_clothes(self):
        return 'Костюм'


class Fabric():
    def __init__(self, name):
        self.__name = name
        self.__clothes = {}

    def add_clothes(self, clothes, count=1):
        self.__clothes[clothes] = self.__clothes.setdefault(clothes, 0) + count

    def __str__(self):
        return f'Фабрика {self.__name}:\n' + \
            '\n'.join(f'{str(key)} * {val}' for key,
                      val in self.__clothes.items())

    def get_fabric_quantity(self):
        sum = 0
        for clothnes, count in self.__clothes.items():
            sum += clothnes.fabric_quantity * count
        return sum


fab = Fabric('Тест')

fab.add_clothes(Suit('Синий', 160), 4)
fab.add_clothes(Suit('Красный', 170))
fab.add_clothes(Coat('Черное', 56), 2)
fab.add_clothes(Coat('Серое', 48))

print(fab)
print('Нужно ткани:', fab.get_fabric_quantity())
