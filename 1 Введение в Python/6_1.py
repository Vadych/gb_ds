import random

min = 1
max = 100
print ("Загадай число от 1 до 100")

while True:
    number = random.randint (min,max)
    print (f'Мое число {number}')
    resp = input("Введите >, < или = ")
    if resp == "=":
        print('Я победил!')
        break
    elif resp == ">":
        max = number - 1
    else:
        min = number + 1
    print (min,max)
    if min > max:
        print ("Ты играл не честно!")
        break