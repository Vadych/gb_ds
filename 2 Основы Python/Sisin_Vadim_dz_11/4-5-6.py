

class Storage:
    __id = 0

    def __init__(self, name, data={}):
        self.name = name
        self.__storage = data

    @classmethod
    def __get_new_id(cls):
        cls.__id += 1
        return cls.__id

    def get_storage(self):
        return self.__storage

    def add_to_storage(self, unit):
        if not unit.get_inventory_number():
            unit.set_inventory_number(Storage.__get_new_id())
        self.__storage[unit] = self.name

    def transfer_to_office(self, unit, office):
        self.__storage[unit] = office

    def get_unit_by_id(self, id):
        for unit, _ in self.__storage.items():
            if unit.get_inventory_number() == id:
                return unit
        return None

    def print_units(self, to_storage=True):
        if len(self.__storage) == 0:
            print('Пока нет техники')
        else:
            for unit, office in self.__storage.items():
                if (office == self.name) == to_storage:
                    print(f'{unit}; Находится - {office}')


class OfficeEquipment:
    def __init__(self, model, inventory_number=None):
        self.model = model
        self._inventory_number = inventory_number

    def set_inventory_number(self, inventory_number):
        self._inventory_number = inventory_number

    def get_inventory_number(self):
        return self._inventory_number

    def __str__(self):
        return f'Техника модели {self.model} c номером {self._inventory_number}'


class Printer(OfficeEquipment):
    def __str__(self):
        return f'Принтер "{self.model}", инв. № {self._inventory_number}'

    def print(self):
        print('Печатаю...')


class Copier(OfficeEquipment):
    def __str__(self):
        return f'Копир "{self.model}", инв. № {self._inventory_number}'

    def copy(self):
        print('Копирую...')


class Scaner(OfficeEquipment):
    def __str__(self):
        return f'Сканер "{self.model}", инв. № {self._inventory_number}'

    def scan(self):
        print('Сканирую...')


class StorageApp:
    USER_ACTION = {
        1: {'label': 'Вывести всю технику', 'action': 'print_all'},
        2: {'label': 'Вывести содержимое склада', 'action': 'print_store'},
        3: {'label': 'Вывести технику не на складе', 'action': 'print_not_store'},
        4: {'label': 'Ввести новую технику', 'action': 'new_unit'},
        5: {'label': 'Передать технику со склада', 'action': 'move_to_user'},
        6: {'label': 'Передать технику на склад', 'action': 'move_to_store'}
    }
    TYPE_UNIT = {
        1: {'label': 'Принтер', 'action': Printer},
        2: {'label': 'Копир', 'action': Copier},
        3: {'label': 'Сканер', 'action': Scaner}
    }

    def __init__(self):
        try:
            with open('store.dat', 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            data = {}
        self.__store = Storage('Главный склад', data)

    def print_store(self):
        self.__store.print_units(True)

    def print_not_store(self):
        self.__store.print_units(False)

    def print_all(self):
        self.print_store()
        self.print_not_store()

    def new_unit(self):
        choice = self.get_user_choice(StorageApp.TYPE_UNIT)
        if not choice:
            return
        model = input('Модель: ')
        count = 0
        while count == 0:
            count = input('Количество: (по умолчанию = 1)') or 1
            try:
                count = int(count)
            except ValueError:
                count = 0
        for i in range(count):
            unit = StorageApp.TYPE_UNIT[choice]['action'](model)
            self.__store.add_to_storage(unit)

    def move_to_user(self):
        self.__store.print_units(True)
        unit = None
        while not unit:
            try:
                number = int(input('Введите инвентарный номер: '))
            except ValueError:
                continue
            unit = self.__store.get_unit_by_id(number)
        office = input('Куда передаем? ')
        self.__store.transfer_to_office(unit, office)

    def move_to_store(self):
        self.__store.print_units(False)
        unit = None
        while not unit:
            try:
                number = int(input('Введите инвентарный номер: '))
            except ValueError:
                continue
            unit = self.__store.get_unit_by_id(number)
        self.__store.add_to_storage(unit)

    def end_app(self):
        with open('store.dat', 'wb') as f:
            pickle.dump(self.__store.get_storage(), f)

    def get_user_choice(self, menu):
        choice = -1
        while not (choice >= 0 and choice <= len(menu)):
            for el_menu in menu:
                print(f'{el_menu}: {menu[el_menu]["label"]}')
            print('0: Выход')
            try:
                choice = int(input('Ваш выбор: '))
            except ValueError:
                print('Недопустимый ввод')
        return choice

    def run(self):
        while True:
            choice = self.get_user_choice(StorageApp.USER_ACTION)
            if not choice:
                self.end_app()
                break
            getattr(self, StorageApp.USER_ACTION[choice]['action'])()


app = StorageApp()
app.run()
