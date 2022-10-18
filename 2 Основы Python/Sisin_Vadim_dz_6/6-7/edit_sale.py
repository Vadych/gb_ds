from cmath import inf
import sys
from utils import FILENAME, get_pos, str_for_file

try:
    start = get_pos(sys.argv[1]) - 10
    new_sum = float(sys.argv[2])
except IndexError:
    print('Введите номер записи и новую сумму')
except ValueError:
    print('Введите номер записи и новую сумму')
    
with open('bakery.csv', 'r+', encoding='utf-8') as file:
    file.seek(start)
    file.write(f'{str_for_file(new_sum)}')
