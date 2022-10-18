from functools import wraps
def val_checker(check_func):
    def checking(func):
        @wraps(func)
        def checking_wrap(*args, **kwargs):
            for arg in args:
                if not check_func(float(arg)):
                    raise ValueError('Не правильный аргумент: ', arg)
            return func(*args, **kwargs)
        
        return checking_wrap
    return checking
    

@val_checker(lambda x: x > 0 )
def new_sum (*args, **kwargs):
    '''Тут вычисляется сумма'''

    print(*kwargs)
    return sum( map(float, args))

print('Имя: ', new_sum.__name__)    
print('Справка: ', new_sum.__doc__)

res = new_sum (1, 4, 50., '453', flag = True, end = 30, start = 'Строка')
print (res)
res = new_sum (1, -4, 50., '453', flag = True, end = 30, start = 'Строка')
