"""
class
"""


# class Car:
#     def __init__(self, color, model, year):
#         self.color = color
#         self.type = model
#         self.year = year
#         self.mileage = 0
#
#     def drive(self, km):
#         self.mileage = self.mileage + km
#         print('dr dr dr')
#
#     def set_null(self):
#         self.mileage = 0
#
#
# almaz = Car('Black', 'Lexus', 2015)
# # print(almaz.__dict__)
# # almaz.drive(500)
# # print(almaz.mileage)
# # almaz.set_null()
# # print(almaz.mileage)
#
# command = ""
# started = False
# while True:
#     command = input("> ")
#     if command == "start":
#         if started:
#             print("Car already started")
#         else:
#             started = True
#             print("Car is ready to go")
#     elif command == "drive":
#         if not started:
#             print("Start the car")
#         else:
#             km = int(input('Distance: '))
#             almaz.drive(km)
#             print(f'you have driven {almaz.mileage} km')
#     elif command == "stop":
#         if not started:
#             print("Car has already stopped")
#         else:
#             started = False
#             almaz.set_null()
#             print(f'Your milage has been updated to {almaz.mileage} km')
#             print("Car has stopped")
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I don't understand command")


# class Car:
#     def __init__(self, color, model, year):
#         self.color = color
#         self.type = model
#         self.year = year
#         self.mileage = 0
#
#     def drive(self, km):
#         self.mileage = self.mileage + km
#         print('dr dr dr')
#
#     def set_null(self):
#         self.mileage = 0
#
#
# car1 = Car('blue', 'lexus', 2000)
# obj = Car('blacj', 'toyota', 2002)
# del удаляет
# del car1
# print(car1.__dict__)

"""
class - incapsulation (private, protected, public)
"""


# class BankAccount:
#     def __init__(self, vendor, account, money):
#         self.vendor = vendor
        # __ делает приватный
        # self.__account = account
        # _ protected method К нему можно достучаться protected attribute money
        # self._money = money

    # Лучший вариант достучаться до приватных атрибутов через getter
#     @property
#     def get_account(self):
#         # Внутри класса можно достучаться до приватных
#         return self.__account
#
#     # Делает сэттер только для get_account
#     @get_account.setter
#     # в def можно изменить get_account на другое
#     def get_account(self, new):
#         self.__account = new
#
#
# almaz = BankAccount('Almaz', '123456', 20000)
# print(almaz.vendor)
# print(almaz._money)
# # print(almaz.__account)  # Выйдет ошибка из-за приватности __
# print(almaz.__dict__)     # Можно узнать на что переименованно __account
# print(almaz._BankAccount__account)  # Из-за приватности переименовывает в _BankAccount__account.
# print(almaz.get_account)        # not collable, это свойство, а не переменная. Лучше так достукиваться до приватных
# print(almaz.get_account)
# almaz.get_account = '123123123'
# print(almaz.get_account)
# print(almaz._money)
# almaz._money = 123234345
# print(almaz._money)
# print(almaz.__dict__)
# almaz._BankAccount__account = '0980998098'
# print(almaz.get_account)
# print(almaz.__dict__)


class Credit:
    def __init__(self, vendor, account, money):
        self.vendor = vendor
        self.__account = account
        self._money = money

    @property
    def get_money(self):
        return self._money

    @get_money.setter
    def get_money(self, years):
        self._money = float(self._money) * 0.2 * float(years) + float(self._money)


ermek = Credit('Ermek', 'Ermek123', 20000)
print(ermek.get_money)
print(ermek.__dict__)
ermek.get_money = 4
print(ermek._money)
print(ermek.get_money)
print(ermek.__dict__)