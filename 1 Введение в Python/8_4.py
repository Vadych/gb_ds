'''
4: Давайте усложним предыдущее задание. 
Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)

Теперь надо добавить новую функцию, которая будет вычислять и возвращать 
полученный урон по формуле damage / armor

Следовательно, у вас должно быть 2 функции:

Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.
Примечание. Функция номер 2 используется внутри функции номер 1 
для вычисления урона и вычитания его из здоровья персонажа. 
'''
import random

def atack_damage (attacker, defender):
    return  attacker['damage'] / defender['armor']
    
def attack(attacker, defender):
    defender['health'] -= atack_damage (attacker, defender)

def create_person(num_player):
    name = input(f"{num_player} player: ")
    player = {'name': name, 'health': random.randint(80,100), 'damage': random.randint(20,50), 'armor': 1.3}
    print (player)
    return player

player1 = create_person(1)
player2 = create_person(2)

print("ATACK!!!")
attack(player1, player2)

print(player1)
print(player2)
