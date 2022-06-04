# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     """Показывает информацию без необходимости вызова этого метода"""
#     def __str__(self):
#         return self.name
#
#
# almaz = Person("Almaz")
# """Показывает имя, т.к мы прописали магический метод __str__"""
# print(almaz)


numbers = list(range(1, 101))


def squares(x): # Возводит в квадрат
    return x**2


new_numbers = list(map(squares, numbers))


def divide(x):  # Выбирает числа которые делятся на 3 и 5
    if x % 3 == 0 and x % 5 == 0:
        return x


result = list(filter(divide, new_numbers))
print(result)

from functools import reduce


def last(a, b):     # Делает сумму чисел
    return a + b


final = reduce(last, result)
print(final)