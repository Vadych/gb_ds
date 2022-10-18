'''
3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 
сделайте импорт в main.py всех функций. 
Вызовите каждую функцию в main.py и проверьте что все работает как надо.
'''

import module10_1
from module10_2 import random_item

module10_1.create_dir()
# input("Продлжим?")
module10_1.delete_dir()


print(random_item([1,2,3]))
print(random_item([]))