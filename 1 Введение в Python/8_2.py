'''
2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
'''

def max_3(*args):
    result = args[0]
    for num in args:
        if num > result:
            result = num
    return result

print (max_3(1, 2,100, 3, -100))