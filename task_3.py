class Cell:
    def __init__(self, box):
        self.box = int(box)

    def __add__(self, other):
        return Cell(self.box + other.box)

    def __sub__(self, other):
        cell_sub = self.box - other.box
        if cell_sub >= 0:
            return Cell(cell_sub)
        else:
            print("К сожалению, клетки больше нет(")

    def __mul__(self, other):
        return Cell(self.box * other.box)

    def __floordiv__(self, other):
        return Cell(self.box // other.box)

    def __str__(self):
        return f"Клетка с {self.box} ячейками"

    def make_order(self, row):
        result = ''
        for _ in range(int(self.box / row)):
            result += "*" * row + '\n'
        result += '*' * (self.box % row)
        return result


cell = Cell(44)
cell_2 = Cell(9)
print(Cell(3))
print("Размер клетки после сложения равен:", cell + cell_2)
print("Размер клетки после вычитания равен:", cell - cell_2)
print("Размер клетки после умножения равен:", cell * cell_2)
print("Размер клетки после умножения равен:", cell // cell_2)
print("Организация ячеек по рядам:", '\n' + cell_2.make_order(3))
