# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,
# например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15) 
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15) 15
# >>> next(odd_to_15) ...StopIteration...

# 2. *(вместо 1) 
# Решить задачу генерации нечётных чисел от 1 до n (включительно), 
# не используя ключевое слово yield.


# Используем yield
def gen_odd_func(max):
    num = 1
    while num <= max:
        yield num
        num += 2
        
gen_odd = gen_odd_func(10)
print (type(gen_odd), list(gen_odd))

# Делаем без функции
n = 10
gen_odd2 = (i for i in range (n + 1))
print (type(gen_odd2))
print (list(gen_odd2))
