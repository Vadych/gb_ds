'''
2: Дан список, заполненный произвольными числами. 
Получить список из элементов исходного, удовлетворяющих следующим условиям:

Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.
'''

import random
first_list = [random.randint(-50, 50) for i in range (20)]
print (first_list)
second_list = [x for x in first_list if x>=0 and x%3 == 0 and x%4 != 0]
print (second_list)