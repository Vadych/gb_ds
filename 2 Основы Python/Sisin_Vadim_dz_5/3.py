# Есть два списка:
# tutors = [
# 'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
# '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А' ]

# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# Количество генерируемых кортежей не должно быть больше длины списка tutors. 
# Если в списке klasses меньше элементов, чем в списке tutors, 
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.

def create_pair (tutors, klasses):
    for i in range(len(tutors)):
        yield tutors[i], klasses[i] if i < len(klasses) else None
        

tutors1 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses1 = ['9А', '7В', '9Б', '9В', '8Б', '10А',  ]

gen_pair = create_pair(tutors1, klasses1)
print (type(gen_pair))
for pair in gen_pair:
    print(pair)