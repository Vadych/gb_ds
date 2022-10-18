'''
2: Создайте модуль. В нем создайте функцию, которая принимает список
и возвращает из него случайный элемент. 
Если список пустой функция должна вернуть None. 
Проверьте работу функций в этом же модуле.
'''
from random import choice

def random_item(list):
    if list:
        return choice(list) 
    return None

if __name__ == '__main__':
    list = [1, 2, 4]
    print(random_item(list))