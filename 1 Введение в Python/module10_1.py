'''
Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
В нем создайте функцию создающую директории от dir_1 до dir_9 
в папке из которой запущен данный код. 
Затем создайте вторую функцию удаляющую эти папки. 
Проверьте работу функций в этом же модуле.
'''

import os
def create_dir():
    for i in range (1,10):
        os.mkdir(os.path.join(os.getcwd(), f'dir_{i}'))

def delete_dir():
    for i in range (1,10):
        os.rmdir(os.path.join(os.getcwd(), f'dir_{i}'))

if __name__ == '__main__':
    delete_dir()