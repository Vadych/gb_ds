import os

users = [
    'Иванов,Иван,Иванович',
    'Петров,Петр,Петрович',
    'Горбунков,Семен,Семеныч'
]

hobby = [
    'скалолазание,охота',
    'горные лыжи',
    'слалом',
    'футбол, тенис'
]

def create_test_data(users, hobbys, test_num):
    with open(f'users{test_num}.csv', 'w') as f:
        for user in users:
            f.write(user + '\n')
    with open(f'hobby{test_num}.csv', 'w') as f:
        for hobby in hobbys:
            f.write(hobby + '\n')
    
create_test_data(users, hobby[:3], 1)    
res = os.system(f'python3 3-4-5.py users1.csv hobby1.csv user-hobby1.txt')
print (res)

create_test_data(users, hobby[:2], 2)    
res = os.system(f'python3 3-4-5.py users2.csv hobby2.csv user-hobby2.txt')
print (res)

create_test_data(users, hobby, 3)    
res = os.system(f'python3 3-4-5.py users3.csv hobby3.csv user-hobby3.txt')
print (res)


