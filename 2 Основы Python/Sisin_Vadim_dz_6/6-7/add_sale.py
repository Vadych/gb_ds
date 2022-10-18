import sys
from utils import FILENAME, get_pos, str_for_file


try:
    sum = float(sys.argv[1])
except IndexError:
    print ('Введите сумму продажи')
except ValueError:
    print ('Введите сумму продажи')
else:
    with open(FILENAME, 'a', encoding='utf-8') as f:
        f.write(f'{str_for_file(sum)}')

