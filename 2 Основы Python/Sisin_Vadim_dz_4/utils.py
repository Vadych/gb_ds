# Написать функцию currency_rates(), принимающую в качестве аргумента код 
# валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. 
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. 
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, 
# посмотреть содержимое ответа. Можно ли, используя только методы класса str, 
# решить поставленную задачу? 
# Функция должна возвращать результат числового типа, например float. 
# Подумайте: есть ли смысл для работы с денежными величинами использовать 
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? 
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. 
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
# Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, 
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

from  decimal import Decimal
from datetime import date
import requests


def get_parametr(string: str, param: str):
    '''
    Выделяет из строки значение первого параметра по шаблону
    <param>Значение<param/>
    '''
    start = string.find('<' + param) + 2 + len(param)
    end = string.find('</' + param)
    return string[start:end].replace(',', '.')
    
def get_date(string):
    '''Выделяет из строки дату по шаблону <ValCurs Date="Дата"'''
    start = string.find('<ValCurs Date="') + 15
    end = string.find('"', start)
    d, m, y = map (int, string[start:end].split('.'))
    return date(y, m, d)

def currency_rates(currency_cod):     
    currency_cod = currency_cod.upper()
    try:
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    except requests.ConnectionError:
        return None, 'Не могу соединиться с сервером'

    if response.status_code != requests.codes.ok:
        return None, 'Ошибка сервера - ' + response.status_code
    
    resp_text = response.text
    date_course = get_date(resp_text)
    # Делим строку по коду валюты на 3 части.
    # Для дальнейшей работы нам понадобится последняя часть.
    
    resp_text = response.text.partition(currency_cod)[2]
    
    if not resp_text:
        return None, 'Валюта не найдена!'
    
    # Оказалось, что некоторые валюты имеют номинал отличный от 1
    nominal = Decimal(get_parametr(resp_text, 'Value'))
    value = Decimal(get_parametr(resp_text, 'Nominal'))
    
    return nominal / value, date_course

if __name__ == '__main__':
    
    print('EUR: ', currency_rates ('eur'))
    print('USD: ', currency_rates ('usd'))
    print('ABC: ', currency_rates('abc'))
    
    