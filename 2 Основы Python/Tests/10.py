
class Test():
    def __init__(self) -> None:
        self.par = 123
        
    @property
    def t_a(self):
        return self.par
    
    @t_a.setter
    def t_a(self, x):
        self.par = x

a = Test()
print(a.t_a)

a.t_a = 3
