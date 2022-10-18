

class Matrix():
    def __init__(self, matrix):
        size_0 = len(matrix[0])
        for line in matrix:
            if len(line) != size_0:
                raise TypeError('Строки имеют разный размер')
        self.__matrix = matrix
    
    @property
    def size_x(self):
        return len(self.__matrix[0])
    
    @property
    def size_y(self):
        return len(self.__matrix)
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.__matrix])
    
    def __add__(self, other):
        if self.size_x != other.size_x or self.size_y != other.size_y:
            raise AttributeError('Матрицы имеют разный размер')
        return Matrix(
            [
                [self.__matrix[y][x] + other.__matrix[y][x] for x in range(self.size_x)]
            for y in range(self.size_y)]
        )
    
    def __getitem__(self, idx):
        return self.__matrix[idx]
        
        
    
m = Matrix([[1,2,3],[4,5,6]])
m2 = Matrix([[1,2,3],[4,5,6]])
print('X = ', m.size_x, ' ; Y = ', m.size_y)

print('Элемент [0, 2] = ', m[0][2])

print('Матрица m:')
print(m)

print('Сумма:')
print(m + m2)

print('Битая матрица')
m2 = Matrix([[1,2,3],[4,5]])

