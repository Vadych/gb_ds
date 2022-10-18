class OrganicCell():
    def check_type(check_func = lambda x, y: True):
        def checked(func):
            def wrapper(self, other):
                if not isinstance(other, OrganicCell):
                    raise TypeError(f'Клетка взаимодействует только с клеткой. Передан {type(other)}')
                if not check_func(self, other):
                    raise ArithmeticError(f'Недопустимые аргументы {self.__size}, {other.__size}')
                return func(self, other)
            return wrapper
        return checked
    
    def __init__(self, count_cells):
        self.__size = count_cells
    
    def __str__(self):
        return f'Клетка на {self.__size} ячеек'
    
    @check_type()
    def __add__(self, other):
        return OrganicCell(self.__size + other.__size)

    @check_type(lambda x, y : x.__size >= y.__size)
    def __sub__(self, other):
        return OrganicCell(self.__size - other.__size)
    
    @check_type()
    def __mul__(self, other):
        return OrganicCell(self.__size * other.__size)
    
    @check_type(lambda x, y : x.__size >= y.__size)
    def __floordiv__(self, other):
        return OrganicCell(self.__size // other.__size)
    
    def __truediv__(self, other):
        return self.__floordiv__(other)
    
    def make_order(self, cells_in_row):
        res = ('*' * cells_in_row + '\n') * (self.__size // cells_in_row)
        if self.__size % cells_in_row:
            res += '*' * (self.__size % cells_in_row)
        else:
            res = res[:-1]
        return res
    

    
    

oc1 = OrganicCell(6)
oc2 = OrganicCell(8)
print(oc1.make_order(2))
print()
print(oc2.make_order(4))
print(oc1 + oc2)
print(oc2 - oc1)


try:
    print(oc1 - oc2)
except ArithmeticError as err:
    print(err.__class__, err)  
    
print(oc2 // oc1)
print(oc2 / oc1)

try:
    print(oc1 / oc2)
except ArithmeticError as err:
    print(err.__class__, err)

try:
    print(oc1 // oc2)
except ArithmeticError as err:
    print(err.__class__, err)

try:
    print(oc1 + 2)
except TypeError as err:
    print(err.__class__, err)