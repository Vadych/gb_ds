# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
 
# [57.8, 46.51, 97, ...]

# A. Вывести на экран эти цены через запятую в одну строку, 
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# B. Вывести цены, отсортированные по возрастанию, новый список не создавать 
# (доказать, что объект списка после сортировки остался тот же).
# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
# возрастанию, написав минимум кода?

price_list = [34.2, 12.4, 20, 0.4, 24.5, 40.54, 39.04, 43.5, 43.56, 134.59, 20.4]

def price_to_str(price):
    return ( f'{int(price)} руб {int(price*100%100):02d} коп')

# А
price_str = ', '.join(map(price_to_str, price_list))
print('Исходный прайс\n', price_str, '\n')

# B
print('Список до сортировки: ', id(price_list))
price_list.sort()
price_str = ', '.join(map(price_to_str, price_list))
print('Список после сортировки', id(price_list))
print(price_str, '\n')

# C
price_list_decr = price_list[::-1]

# D
price_str = ', '.join(map(price_to_str, price_list_decr[:5]))
print('5 самых высоких цен\n', price_str)