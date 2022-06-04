"""
Class
"""# class Dog:
#     name = 'juchka'
#     breed = 'buldog'
#
#
# dog1 = Dog()
# dog2 = Dog()
# dog1.name = 'Sharik'
# print(dog1.name)
# print(dog2.name)
# print(dog1.__dict__)        # Магический метод, Dunder method
# print(dog2.__dict__)
# Dog.name = 'Tuzik'
# print(dog1.name)
# print(dog2.name)
# print(dog2.__dict__)
# print(dog1.__dict__)
from functools import reduce


"""
 Функции внутри Классов
"""
# class Dog(object):
#     breed = 'buldog'
#
#     def get_bark(self):
#         print('gav gav')
#
#
#     def get_eat(self, food):
#         print(f'nyam nyam {food}')
#
# dog1 = Dog()
# dog2 = Dog()
# dog1.get_bark()     # Можно вызывать функции классов через методы
# dog2.get_eat('bones')
# dog1.get_eat('fresh meat')

"""
Dunder method __init__ ~ Магический метод __init__
"""


# class Student:
#     name_rector = 'Chynybaev'
#     def __init__(self, name, age, group):
#         self.name = name
#         self.age = age
#         self.group = group
#
#
#     def get_info(self):
#         print(f'{self.name}', {self.age}, {self.group})
#
# nodira = Student("Nodira", 23, 'python')
# daniel = Student("Daniel", 21, 'python_bootcamp')
# nodira.subject = 'algebra'
# Student.name_rector = 'Next'
# print(nodira.age)
# print(daniel.__dict__)
# print(nodira.subject)
# print(Student.name_rector)
# print(nodira.name_rector)
# nodira.get_info()
# daniel.get_info()


subject_nodira = {'algebra':80, 'chemistry':70, 'physics': 95}
subject_daniel = {'algebra':56, 'chemistry':60, 'physics': 80}


class Student:
    def __init__(self, name, age, group, subject):
        self.name = name
        self.age = age
        self.group = group
        self.subject = subject

    def get_info(self):
        print(f'{self.name}', {self.age}, {self.group})

    def get_avg(self):
        avg = (sum(self.subject.values()))/len(self.subject)
        return avg/len(self.subject)

    def get_grade(self):
        if self.age >= 18 and self.age <= 19:
            return 'grade 1'
        elif self.age >= 20 and self.age <= 21:
            return 'grade 2'
        elif self.age >= 22 and self.age <= 23:
            return 'grade 3'
        elif self.age >= 24 and self.age <= 25:
            return 'grade 4'
        else:
            return 'Не соответствует возрасту студентов'


nodira = Student("Nodira", 23, 'python', subject_nodira)
daniel = Student("Daniel", 21, 'python_bootcamp', subject_daniel)
print(nodira.get_avg())
print(nodira.get_grade())

