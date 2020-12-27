###################################################
# Corey Schafer
import datetime


class Employee(object):
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'
    # regularmethod используется для изменения атрибутов инстанса класса

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)
    # staticmethod не используется за пределами класса
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
            return True
    # classmethod используется для изменения атрибутов класса
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amt = 1.07

    def __init__(self, first, last, pay, employees=None):
        # Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'-->{emp.fullname()}')


print(f'Number of employees before the initiation:  {Employee.num_of_emps}')

emp1 = Employee('Corey', 'Schafer', 70000)
emp2 = Employee('Mark', 'Mendela', 100000)
emp3 = Employee.from_string('Corey-Schafer-82000')
dev1 = Developer('Misha', 'Clark', 60000, 'Python')
dev2 = Developer('Lisa', 'Bark', 10000, 'Java')
mgr1 = Manager('Anthony', 'Hopkins', 20000, [dev1])
mgr2 = Manager('Sue', 'Smith', 20000)

print(f'Number of employees after the initiation:  {Employee.num_of_emps}')

print(f'emp1 pay before apply_raise(): {emp1.pay}')

emp1.apply_raise()

print(f'emp1 pay after apply_raise(): {emp1.pay}')

Employee.set_raise_amt(1.2)
emp1.apply_raise()

print(f'emp1 pay after set_raise_amt() and apply_raise(): {emp1.pay}')

print(f'{datetime.date(2019, 7, 21)} is_workay(): {Employee.is_workday(datetime.date(2019, 7, 21))}')

mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.print_emps()

print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))
print(isinstance(mgr1, Manager))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Developer, Manager))

print(repr(emp1))
print(emp1.__repr__())
print(str(emp1))
print(emp1.__str__())

print(emp1+emp2)
print(len(emp1))


class Employee2(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@email.com'
        # self.fullname = f'{first} {last}'

    # property позволяет обращаться к методу как к атрибуту
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    # .setter позволяет изменять атрибуты, обращаясь к методу как к атрибуту,
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    # .deleter позволяет удалять атрибуты, обращаясь к методу как к атрибуту,
    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp21 = Employee2('John', 'Smith')
emp21.first = 'Jim'
emp21.fullname = 'Corey Schafer'  # нужен @.setter

print(emp21.first)
print(emp21.last)
print(emp21.email)  # нужен @property
print(emp21.fullname)  # нужен @property

del emp21.fullname  # нужен @.deleter
print(emp21.first)
print(emp21.last)
print(emp21.email)
print(emp21.fullname)
###################################################
# Tceh
# ООП
# Сущность, на которой построено ООП - концепция класса.
# Класс - это шаблон, по которому будет воспроизведен обьект
# Пример класса - словарь. Внутренне все словари устроены одинаково. Но при этом это разные словами.Отличаются они только теми данными, которые мы в них положим.
# Пример класса - бмв. Все бмв спущенные с конвеера в одном году устроены одинаково. Но при этом это разные машины.
# Обьекты класса подобны по структуре друг другу. Словари словарям, списки спискам, машины машинам.

# Принципы ООП: наследование, инкапсуляция, полиморфизм[, абстракция]
#
# Наследование позволяет переиспользовать тот код, который мы уже когда то использовали.
# Использование того когда, который уже есть - делает разработку быстрее
# Пример: есть функция которая складывает 2 числа и выводит их. Задача: нужно вывести 2 числа, но не складывать. Или только сложить их, но не выводить.
# Переиспользовать код, написанный в функции - нельзя. Можно либо вызвать функию, либо не вызывать функцию. Наследование позволяет переиспользовать часть уже имеющейся логики.
# Все обьекты можно разделить на несколько типов, и все они наследуются от objects.


class Parent(object):
    def __init__(self):
        print('parent initied')
        self.value = 'parent'

    def do(self):
        print('parend do(): {}'.format(self.value))


class Child(Parent):
    def __init__(self):
        print('child initied')
        self.value = 'child'


parent = Parent()
parent.do()

child = Child()
child.do()


class Calc(object):
    def __init__(self, number):
        self.number = number  #

    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('--------------')
        print('number is', value_to_print)
        print('--------------')

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)


class CalcExtraValue(Calc):
    def calc_value(self):
        return self.number - 100


c = Calc(3)
c.calc_and_print()

c1 = CalcExtraValue(3)
c1.calc_and_print()
# Переопределить в дочернем классе можно любой метод. Можно переопределить конструктор, и print_number(то, как выводится), и calc_value(то, как вычисляется). А если переопределить главный метод - сalc_and_print, то можно вообще переопределить логику конструктора.

# Функция такого сделать не позволяет. Если есть функция, то можно ее вызвать, можно передать ей разные аргументы, и изза разных аргументов она выдасть разные значения. До убавить или прибавить какую то логику к функции не получится.


# Инкапсуляция позволяет скрывать реализацию методов, что делает их использование удобным и безопасным для конечного разработчика. В пайтоне не работает.
class Example(object):
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
        print('{}{}{}'.format(self.a, self._b, self.__c))

    def call(self):
        print('called!')


example = Example()
# print(example.a) >>> 1
# print(example._b) >>> 2
try:
    print(example.__c)
except AttributeError as ex:
    print(ex)  # >>> AttributeError: 'Example' object has no attribute '__c'
# Ошибка вылезет потому что self.c перезапишется как _Example_.c
# Есть 3 типа имен.
# 1 - обычное, без подчеркиваний. Можно использовать где угодно
# 2 -  с одним подчеркиваний. Условная договоренность между людьми, что их лучше не использовать
# 3 - с двумя подчеркиваниями. Вообще не трогайте это, оно недоступно.
# Зачем делать это?
# Защита от дурака.


# Полиморфизм позволяет использовать функции по разному в зависимости от типа их входных аргументов.
# Утиная типизация. Если что-то выглядит как утка и крякает как утка, то скорее всего это утка.  Проблема в том что нельзя узнать - утка это или нет.
# len() - лен совершенно спокойно работает с [], {} и ""
# len(item) - лен ожидает что обьект item будет таким, у которого можно найти длинну. Ее не интерисует тип обьекта,  ее интерисует только то чтобы от него можно было взять длину. Но проблема в том что не от каждого обьекта можно взять длину.
class Parent(object):
    def call(self):
        print('parent')


class Child(Parent):
    def call(self):
        print('child')


class Example(object):
    def call(self):
        print('ex')


def call_to_object(obj):
    obj.call()


# Чего же мы ожидаем от функции call_to_object(), чтобы она что сделала?
# Чтобы она позвонила обьекту obj.
# Как функция call_to_object() позвонит обьекту obj?
# Нужно чтобы у обьекта obj был метод .call.  Если у обьекта obj не будет метода .call, то произойдет ошибка
# Какие аргументы может принимать функция call_to_object()?
# Любые, у которых есть метод .саll
# Утиная типизация здесь в том, что нам неважно что такое obj. Но если у него есть метод .call, то это нам подходит.
call_to_object(Child())  # >>> child
call_to_object(Parent())  # >>> parent
call_to_object(Example())  # >>> ex
# Как Пайтон может узнать, что мы ему вообще передаем? Как Пайтон может узнать что у передаваемого обьекта есть метод .call?
# Никак, Пайтон не может об этом никак узнать
# Кто может об этом узнать?
# Программист должен брать на себя ответственность, что он передает правильные аргументы, в правильные функции, правильные типы подставляет в нужные места.
# Пример дак тайпинга в Пайтоне:


def sum_two_objects(one, two):
    return one + two
# Пайтон умеет складывать списки, числа, строки и кортежи, поэтому их можно передавать в функцию как аргументы.
# В эту функцию можно передать все что складывается между собой. Если вы знаете что чтото можно складывать, то это можно складывать, неважно какого это типа.
# Полиморфизм позволяет использовать функции по разному в зависимости от типа их входных аргументов.
# Числа - складывание. Строки - конкатенация. Списки - обьединение каких то множеств. Внутри все устроено по разному, а внешняя оболочка (знак + )  - одинаковая
