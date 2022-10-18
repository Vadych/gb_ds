# Представлен список чисел. Определить элементы списка, не имеющие повторений. 
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, 
# например:
#     src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] 
#     result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

from random import randrange
from sys import getsizeof
import time

# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] 
num = 10000
src = [randrange(num) for i in range(num)]

# Вариант из методички
start = time.time()
unique_set = set()
processed_set = set()

for el in src:
    if el not in processed_set:
        unique_set.add(el)
    elif el in unique_set:
        unique_set.discard(el)
    processed_set.add(el)
        
result = [el for el in src if el in unique_set]
finish = time.time()
print (len(result))
print ('Время - ', finish - start)
print ('Память - ', getsizeof(unique_set) + getsizeof(processed_set))

# Вариант со словарем
start = time.time()
processed_dict = {}
for el in src:
    processed_dict[el] = processed_dict.setdefault(el, 0) + 1

result = [el for el in src if processed_dict[el] == 1]
finish = time.time()
print (len(result))
print ('Время - ', finish - start)
print ('Память - ', getsizeof(processed_dict))

# Вариант в лоб
start = time.time()
result = [el for el in src if src.count(el) == 1]
finish = time.time()
print (len(result))
print ('Время - ', finish - start)
print ('Память - 0')
