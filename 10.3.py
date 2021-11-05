

class Cell:
    def __init__(self, nums):
        self.nums = nums #13

    def make_order(self, rows): #5
        return '\n'.join(['&' * rows for _ in range(self.nums // rows)]) + '\n' + '&' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("sum of cell is: ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("sutraction of cell is: ")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "ячеек в первой клетке меньше второй, вычетание невозможно"

    def __mul__(self, other):
        print("multiply of cell is: ")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Truediv of cell is")
        return Cell(self.nums // other.nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))