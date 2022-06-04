"""
Моносостояние
"""


# class Car:
#       # Моносостояние, даёт одно значание на все объекты. В случае изменения, изменяется во всех объектах
#     __attrs_car = {
#         'speed': 200,
#         'color': 'red'
#     }
#
#     def __init__(self):
#         self.__dict__ = self.__attrs_car
#
#
# car1 = Car()
# print(car1.__dict__)
#
# class Car:
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#         self.__dict__['year'] = 1996
#
#
# car1 = Car('red', 400)
# car2 = Car('blue', 100)
# print(car1.__dict__)
# print(car2.__dict__)
# car2.year = 2000
# print(car1.__dict__)
# print(car2.__dict__)


"""Dunder methods от стлова double underscore '__a__'"""


# class Size:
#
#     # Всегда обрабатывает в первую очередь
#     # def __new__(cls, *args, **kwargs):
#     #     print('first')
#
#     def __init__(self, size):
#         self.size = size
#         print('second')
#
#
# # При проверке выведет first так как вписывает его в new, даже если прописать его после init
# a = Size(12)


# class Size:
#
#     def __init__(self, size):
#         self.size = size
#
#     # Не нужно будет через .Size выходить на число объекта.
#     def __add__(self, other):
#         # Для того чтобы два объекта можно было прибавить, проверяет на то что он в классе xthtp true false
#         if isinstance(other, Size):
#             return self.size + other.size
#         # Для того чтобы числа к объекту можно было прибавить
#         return self.size + other
#
#     # Функционал такой же как и в __add__, только наоборот поэтому пишется 1 к 1му и автоматом переворачивает
#     def __radd__(self, other):
#         if isinstance(other, Size):
#             return self.size + other.size
#         return self.size + other
#
#
# a = Size(12)
# b = Size(14)
# print(a + b)
# print(2 + a)


""" Пример"""


class Size:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        if isinstance(other, Size):
            return str(self.size) + str(other.size)
        return str(self.size) + str(other)

    def __radd__(self, other):
        if isinstance(other, Size):
            return str(self.size) + str(other.size)
        return str(self.size) + str(other)


a = Size(12)
b = Size(14)
print(a + 'aba')
print(a + b)
print('aba' + a)
print(a + 2)

"""
ДЗ
__truediv__ деление, __mul__ умножение, __sub__ минус. Определить этя три дандер метода.

class Diagram:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

a = Diagram(5, 4)
b = Diagram(3, 2)
# a - b должен вытащить (2, 2)

Также с делением, умножением и вычетанем
"""


