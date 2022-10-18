import os
import random

for i in range(10):
    sum = random.randint(100, 10000000) / 100
    os.system(f'python3 add_sale.py {sum}')

print ('Добавлено')
print ('Вывожу все')
os.system('python3 show_sales.py')
print ('Вывожу с 8й')
os.system('python3 show_sales.py 8')
print ('Вывожу с 3 по 5')
os.system('python3 show_sales.py 3 5')
print('Перезаписываю 3')
os.system('python3 edit_sale.py 3 1000')
print ('Вывожу с 3 по 5')
os.system('python3 show_sales.py 3 5')


