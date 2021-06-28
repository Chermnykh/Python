import math


class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        print('Сложение комплексных чисел: ')
        first_sum = self.a + other.a
        second_sum = self.b + other.b
        return ComplexNumber(first_sum, second_sum)

    def __mul__(self, other):
        print('Произведение комплексных чисел: ')
        first_mul = self.a * other.a - self.b * other.b
        second_mul = self.b * other.a + self.a * other.b
        return ComplexNumber(first_mul, second_mul)


res_1 = ComplexNumber(1, 2)
res_2 = ComplexNumber(3, 4)

print(f"{res_1} + {res_2} = ", res_1 + res_2)
print(f"{res_1} * {res_2} = ", res_1 * res_2)
