
class IntListErr(Exception):
    def __init__(self, err_element):
        self.err_element = err_element
    
    def __str__(self):
        return f'Ошибочный аргумент {self.err_element}'


class IntList(list):
    
    @classmethod
    def check_element(cls, element):
        try:
            element = int(element)
        except ValueError:
            raise IntListErr(element)
        return element
        
        
    def append(self, element):
        return super().append(IntList.check_element(element))
        
    
    def extend(self, new_list):
        for el in new_list:
            IntList.check_element(el)
        return super().extend(new_list)
        
    def insert(self, idx, element):
        return super().insert(idx,IntList.check_element(element))
    
        
        
test = IntList()
while True:
    el = input('Введите целое число: ')
    if not el:
        break
    try:
        test.append(el)
    except IntListErr as err:
        print(err)
        
print (test)