"""
Модуль datetime
"""

from datetime import (datetime, date,
                      timedelta, time
                      )

# time_now = datetime.now()
#
# date_today = date.today()
# hour = time_now.time().hour
# minute = time_now.time()minute
# second = time_now.time().second
#
# print(time_now)
# print(time_now.time())
# print(date_today)
# print(hour)

# date_today = date.today()
# time_now = datetime.now()
# print(date_today.year)
# print(date_today.month)
# print(date_today.day)

# # datee = date(2022, 2, 22)
# datee = datetime(2022, 2, 12, 9, 55, 59, 12)
# # datee1 = datetime(2021, 2, 12, 9, 55, 59, 12)
# datee1 = datetime(2021, 2, 12)
# # timedelta преобразует в формат день и время
# time_delta = timedelta(weeks=5, hours=3, seconds=567)
# times = timedelta(weeks=1, hours=2, microseconds=55555555)
# print(datee - datee1)
# print(time_delta)
# print(time_delta - times)
# print(time_delta + times)
# print(time_delta + datee)

"""timestamp"""
# timestamp = 1545730073
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)
# print(type(dt_object))
# data = '01-01-2022'
# # y - использует два числа от года, Y - использует все числа года
# data1 = datetime.strptime(data, '%d-%m-%Y')
# print(data1)
# a = datetime.now()
# data2 = a.time().strftime('%Y-%m-%d')
# print(data2)
# print(type(data2))

"""импортируем pytz"""
import pytz

"""Using timezone via pytz"""
# local = datetime.now()
# print('local time: ', local)
# timezone_ny = pytz.timezone('America/Chicago')
# tz_ch = pytz.timezone('China')
# ny = datetime.now(timezone_ny)
# print('NY: ', ny)

"""Пример"""
# class Person:
#     def __init__(self, name, age, surname='Empty'):
#         self.name = name
#         self.age = age
#         self.surname = surname
#
#
# # Если проименовал один, то нужно проименовывать все остальные
# almaz = Person(age=29, surname='Durusaliev', name='Almaz')
# print(almaz.__dict__)
# # Выведт заполненные значения по порядку как в def
# almaz = Person(29, 'Durusaliev', 'Almaz')
# print(almaz.__dict__)


"""Задание"""


class Person:
    def __init__(self, name, age, surname='Empty'):
        self.name = name
        self.age = age
        self.surname = surname

    def cur_age(self):
        born_date = datetime.now().year - almaz.age
        new_year = int(input('Enter a year: '))
        if new_year >= born_date:
            almaz.age = new_year - born_date
        elif new_year < born_date:
            print("Can't enter a year less than age")
        return almaz.age


almaz = Person(name='Almaz', surname='Durusaliev', age=20)
# print(almaz.__dict__)
# cur_time = datetime.now()
# print(cur_time)
# born_date = cur_time.year - almaz.age
# print(born_date)
# print(type(born_date))
# new_year = 2030
# almaz.age = new_year - born_date
# print(almaz.__dict__)
print(almaz.__dict__)
almaz.cur_age()
print(almaz.__dict__)
