

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    
    def __str__(self):
        return f'{self.re}: {self.im}'
    
    def __add__(self, other):
        return Complex (self.re + other.re, self.im + other.im)
    
    def __mul__(self, other):
        return Complex(
            self.re * other.re - self.im * other.im,
            self.im * other.re + self.re * other.im
        )
    

t1 = Complex(1, 1)
t2 = Complex(2, 2)
print(t1+t2)

t3 = Complex (0, 1)
print(t3*t3)