class Person:
    # def __init__(self, name, surname):
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    # Показывает информацию об объекте
    def information(self):
        return f'{self.name}, {self.surname}, {self.qualification}'

    """ def __del__ удаляет, но когда он проходиться по объектам выдаёт ошибку, т.к не учитывет другие объекты"""
    # def __del__(self, self_2, self_3):
    #     if self.qualification < self_2.qualification and self.qualification < self_3.qualification:
    #         print(f'До свидания, мистер {self.name} {self.surname}')
    #         del self
    #     elif self_2.qualification < self.qualification and self_2.qualification < self_3.qualification:
    #         print(f'До свидания, мистер {self_2.name} {self_2.surname}')
    #         del self_2
    #     elif self_3.qualification < self.qualification and self_3.qualification < self_2.qualification:
    #         print(f'До свидания, мистер {self_3.name} {self_3.surname}')
    #         del self_3
    #     else:
    #         print('Нет менее квалифицированного человека')

    """ Прописывает текст по всем объектам вне зависимости от того вызываем мы его или нет"""
    def __del__(self):
        print(f'до свидания, мистер {self.name} {self.surname}')

# almaz = Person('Almaz', 'Durusaliev')
# almaz.qualification = 10
# ermek = Person('Ermek', 'Durusaliev')
# ermek.qualification = 5
# zakir = Person('Zakir', 'Lamiev')
# zakir.qualification = 90
almaz = Person('Almaz', 'Durusaliev', 10)
ermek = Person('Ermek', 'Durusaliev')
zakir = Person('Zakir', 'Lamiev', 90)

print(zakir.information())

"""Удаляет объект с самим маленьким значением квалификации"""
if almaz.qualification < ermek.qualification and almaz.qualification < zakir.qualification:
    print(f'Уважаемый {almaz.name} {almaz.surname}, к сожалению мы должны с вами попрощаться')
    del almaz
elif ermek.qualification < almaz.qualification and ermek.qualification < zakir.qualification:
    print(f'Уважаемый {ermek.name} {ermek.surname}, к сожалению мы должны с вами попрощаться')
    del ermek
elif zakir.qualification < almaz.qualification and zakir.qualification < ermek.qualification:
    print(f'Уважаемый {zakir.name} {zakir.surname}, к сожалению мы должны с вами попрощаться')
    del zakir
else:
    print('Нет менее квалифицированного человека')

# Вызывает __del__
del almaz

finish = input('Press enter ')
