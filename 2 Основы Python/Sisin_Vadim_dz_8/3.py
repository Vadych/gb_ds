from functools import wraps

def type_loger(func):
    @wraps(func)
    def loging(*args, **kwargs):
        '''Это логинг из декоратора'''
        res = func(*args, **kwargs)
        print (f'{func.__name__}(', end='')
        print (', '.join([f'{i}: {type(i)}' for i in args]), end='')
        if args and kwargs: print(', ')
        print (', '.join([f'{i} = {kwargs[i]}: {type(i)}' for i in kwargs]), ')', end = '')
        print (f' -> {type(res)}')
        return res
    
    return loging
    
@type_loger
def new_sum (*args, **kwargs):
    '''Тут вычисляется сумма'''

    print(*kwargs)
    return sum( map(float, args))

print('Имя: ', new_sum.__name__)    
print('Справка: ', new_sum.__doc__)

res = new_sum (1, 4, 50., '453', flag = True, end = 30, start = 'Строка')
print (res)
