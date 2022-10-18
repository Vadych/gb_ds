'''
1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой
музыкальной группы, например:
С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
вывести результаты в терминал. 
Записать результаты в файлы group.json, group.pickle соответственно. 
В файле group.json указать кодировку utf-8.
'''
from base64 import encode
import json, pickle

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок','year': 2016},
    {'name': 'Шапито','year': 2014}]
    }

json_favorite = json.dumps(my_favourite_group)
print(type(json_favorite))
pickle_favorite = pickle.dumps(my_favourite_group)
print(pickle_favorite)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group,f)
    print('json')
    
with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group,f)
    print('pickle')