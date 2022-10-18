'''
3: Давайте опишем пару сущностей player и enemy через словарь, 
который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50.
Поэкспериментируйте с значениями урона и жизней по желанию. 
Теперь надо создать функцию attack(person1, person2). 
Примечание: имена аргументов можете указать свои. 
Функция в качестве аргумента будет принимать атакующего и атакуемого. 
В теле функция должна получить параметр damage атакующего и отнять это количество
от health атакуемого. Функция должна сама работать со словарями и изменять их значения.
'''
import random

def attack(attacker, defender):
    defender['health'] -= attacker['damage']

def create_person(num_player):
    name = input(f"{num_player} player: ")
    player = {'name': name, 'health': random.randint(80,100), 'damage': random.randint(20,50)}
    print (player)
    return player

player1 = create_person(1)
player2 = create_person(2)

print("ATACK!!!")
attack(player1, player2)

print(player1)
print(player2)
