class Diagram:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if isinstance(other, Diagram):
            return self.x - other.x, self.y - other.y

    def __mul__(self, other):
        if isinstance(other, Diagram):
            return self.x * other.x, self.y * other.y

    def __truediv__(self, other):
        if isinstance(other, Diagram):
            return self.x / other.x, self.y / other.y


a = Diagram(5, 4)
b = Diagram(3, 2)
print(a / b)
print(a * b)
print(a - b)
