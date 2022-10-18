# Представлен список чисел. 
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] 
# result = [12, 44, 4, 10, 78, 123]

# Подсказка: использовать возможности python, изученные на уроке. 
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

from random import randrange
import time
def gen_pair(src):
    pred = None
    for el in src:
        yield pred, el
        pred = el

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] 
        
src = [randrange(1000) for i in range (10000000)]
# Решение через генератор с доступом по индексу. Не придумал способа,
# как получить сразу два элемента за один проход

start = time.time()
result = [src[i] for i in range(1, len(src)) if src[i-1] < src[i]]
finish = time.time()
print (len(result))
print (finish - start)

# Решение с отказом от доступа по индексам, которое медленное.
# Мне кажется это наиболее быстрое решение как по скорости, так и по памяти

start = time.time()
gen_res = gen_pair(src)
next(gen_res)
result = [el for pred, el in gen_res if pred < el]
finish = time.time()
print (len(result))
print (finish - start)
