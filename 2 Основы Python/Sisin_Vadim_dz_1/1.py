
# Реализовать вывод информации о промежутке времени в зависимости от его 
# продолжительности duration в секундах:
#     a. до минуты: <s> сек;
#     b. до часа: <m> мин <s> сек;
#     c. до суток: <h> час <m> мин <s> сек;
#     d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


list_interval = [['дн ', 24*60*60], ['час ', 60*60], ['мин ', 60], ['сек',1]]
test_duration = [53, 153, 4153, 399600, 400153]
for duration in test_duration:
    print('duration = ', duration)
    duration_str = ''
    for label, interval in list_interval: 
        interval_digit = duration // interval
        # Проверяем есть ли разряд в этом интервали и есть ли разряды выше
        # Если нет требования выводить нулевые разряды в середине строки,
        # то проверку на длину строки можно убрать
        if interval_digit or duration_str:
            duration_str += f'{interval_digit} {label}'
            duration %= interval          
    print(duration_str)
    
'''
Альтернативное решение.
Преобразование числа в строку вынести в функцию.
В цикле соответсвенно вызывать только функцию и печатать результат
for duration in test_duration:
    print('duration = ', duration)
    print(duration_to_str(duration))
'''
