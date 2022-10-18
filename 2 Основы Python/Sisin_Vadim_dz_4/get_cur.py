from utils import currency_rates
import sys

if len(sys.argv) == 1:
    print ('Тестовый запуск')
    print('ABC: ', currency_rates('abc'))
    print('USD: ', currency_rates ('usd'))
    print('EUR: ', currency_rates ('eur'))
    
else:
    value, date = currency_rates(sys.argv[1])
    if value: # Значение получено, ошибок нет
        print (value, date)
        pass
    else: # Была ошибка, описание в date
        print (date)
