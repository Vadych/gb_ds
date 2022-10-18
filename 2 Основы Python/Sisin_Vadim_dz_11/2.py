

class DivZero(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    
    def __str__(self):
        return 'На 0 делить нельзя!'

while True:
    x = input('Введите делитель 100: ')
    if x == '':
        break
    try:
        x = int(x)
        if x == 0:
            raise DivZero
        print(100 / x)
    except ValueError:
        print('Введите число')
    except DivZero as err:
        print (err)