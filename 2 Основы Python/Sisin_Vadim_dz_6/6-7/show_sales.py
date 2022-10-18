from cmath import inf
import sys
from utils import FILENAME, get_pos

if len(sys.argv) == 1:
    start = 1
    end = inf
elif len(sys.argv) == 2:
    start = get_pos(sys.argv[1]) - 10
    end = inf
else:
    start = get_pos(sys.argv[1]) - 10
    end = get_pos(sys.argv[2])


with open(FILENAME, 'r', encoding='utf-8') as file:
    file.seek(start)
    line = file.readline()
    while line and file.tell() <= end:
        print(f'{float(line): 9.2f}')
        line = file.readline()

