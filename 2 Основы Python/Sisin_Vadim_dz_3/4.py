# Написать функцию thesaurus_adv(), 
# принимающую в качестве аргументов строки в формате «Имя Фамилия» 
# и возвращающую словарь, в котором ключи — первые буквы фамилий, 
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
#     >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
#     {
#     "А": {
#     "П": ["Петр Алексеев"]
#     }, "И": {
#     "И": ["Илья Иванов"] },
#     "С": {
#     "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"]
#     } }

# Как поступить, если потребуется сортировка по ключам?

from unicodedata import name


def thesaurus_adv(*names, sort = False):
    res_dict = {}
    if sort:
        names = sorted(names, key = lambda x : (x.split()[1], x.split()[0]))
    for name in names:
        f_name, l_name = name.split()
        res_dict.setdefault(l_name[0],{}).setdefault(f_name[0],[]).append(name)
    return res_dict


test_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", 
             "Илья Иванов", "Анна Савельева", "Виктор Алексеев", "Виталий Алексеев"]

print (thesaurus_adv(*test_list, sort=True))
