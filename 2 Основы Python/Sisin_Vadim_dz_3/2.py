# Написать функцию num_translate(), переводящую числительные от 0 до 10 
# c английского на русский язык. Например:
#     >>> num_translate("one") "один"
#     >>> num_translate("eight") "восемь"
# Если перевод сделать невозможно, вернуть None. 
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: 
# какой тип данных выбрать, в теле функции или снаружи.

# Доработать предыдущую функцию в num_translate_adv(): 
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной. Например:
#     >>> num_translate_adv("One") "Один"
#     >>> num_translate_adv("two") "два"
def num_translate_adv(eng_word):
    tranlate_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    res = tranlate_dict.get(eng_word.lower())
    if res:
        if eng_word.istitle():
            return res.title()
        else:
            return res
    
    return None
        
test_list = ['one', 'Two', 'three', 'Four', 'five', 'Six', 
             'seven', 'Eight', 'nine', 'Ten', 'None']

for word in test_list:
    print(word, ' - ', num_translate_adv(word))
