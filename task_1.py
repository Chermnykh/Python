class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return '\n'.join('\t'.join([str(item) for item in line]) for line in self.param)

    def __add__(self, other):
        if len(self.param) != len(other.param):
            raise ValueError('Ошибка размерностей матрицы')
        for index, el in enumerate(self.param):
            if len(el) != len(other.param[index]):
                raise ValueError('Ошибка размерностей матрицы')
        m = [[int(self.param[line][item]) + int(other.param[line][item])
              for item in range(len(self.param[line]))] for line in range(len(self.param))]
        return Matrix(m)


mx_1 = [[31, 22, 3], [37, 43, 5], [34, -54, 5]]
mx_2 = [[5, 32, 3], [4, 6, 8], [64, -8, 3]]

matrix_1 = Matrix(mx_1)
matrix_2 = Matrix(mx_2)
new_matrix = matrix_1 + matrix_2

print('Первая матрица:\n', matrix_1, sep='')
print('Вторая матрица:\n', matrix_2, sep='')
print('Сумма матриц:\n', new_matrix, sep='')
