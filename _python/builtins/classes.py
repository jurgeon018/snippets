# super() - конструкция, которая позволяет явно обращаться к методам родителей из дочернего класса.Еще больше упрощает переиспользование кода.
# Если в ребенке есть метод, который называется так же как и метод в классе родителя, то он его переопределяет, и больше обратиться к методу родителя он не может. Для того чтобы продолжать работу с логикой, которая описана в родительском методе с таким же названием, можно переиспользовать ее при помощи явного вызова super().


class Calc(object):
    def __init__(self, value):
        print('Calc constructor is called')
        self.value = value

    def count(self):
        return self.value * 8 + 9


class DoubleCalc(Calc):
    def count(self):
        return 2 * super().count()


class ExtendedCalc(DoubleCalc):
    def __init__(self, value, k=1):
        super().__init__(value)
        print('Extender', self.value)
        self.k = k

    def count(self):
        return -1 * self.k * super().count()


c = Calc(1.4)
e = ExtendedCalc(8, k=2)
d = DoubleCalc(8)
print(c.count())
print(e.count())


# Method Resolution Order
# Есть методы, и они вызываться в определенном порядке
# Как понять какой метод когда должен вызваться?
# Порядок вызова методов определяется ClassName.__mro__
print(ExtendedCalc.__mro__)


# Математические магические метдоды
# Пример - __init__. Этот метод инициализирует переменные обьекта класса во время его создания
# Все магические методы выгдят одинаково - __имя__
# Как как сложить любой пайтон обьект с любым пайтон обьектом?


class Test(object):
    def __add__(self, other):
        return '0_0' + str(other)


t = Test()
print(t + 2)
print(Test() + '2' + 'sdf')


class BadStr(str):
    def __add__(self, other):
        return str(self) + str(other)


t = BadStr('some')
print(t + 2)


class MathObject(object):
    def __init__(self, value=2):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __eq__(self, other):
        return self.value == other

    def __ge__(self, other):
        return self.value >= other

    def __lt__(self, other):
        return self.value < other

    def __mul__(self, other):
        return self.value * other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        return self.value == other


t = MathObject()
print(t + 4)  # == print(t.__add__(4))


class MathObject:
    def __init__(self):
        self.value = 2

    def __str__(self):
        return '<MathObject: {}>'.format(self.value)


t = MathObject()
print(t)
# Когда я делаю print(t), то я попадаю в магический метод __str__
# Для того чтобы напечатать какой то экземпляр класса, нужно сначала превратить его в строку при помощи магического метода __str__


# Магические методы для работы с индексированием, слайсами и последовательностями(cписки, строки, кортежи и словари)

# Какие пайтон-обьекты можно складывать между собой?
# Те, в классе которых переопределен метод __add__
# У какого пайтон-обьекта можно найти длину?
# Того, в классе которого переопределен метод __len__
# Утиная типизация в пайтоне: если у обьекта, с которым мы работаем есть такой магический метод, то он сработает. Если такого магического или обычного метода нет, то он не сработает.


class MathObject(object):
    def __init__(self):
        self.value = 2

    def __contains__(self, item):
        return item == self.value


t = MathObject()
print(2 is t)


class MathObject(object):
    def __init__(self):
        self.value = 2


t = MathObject()
print(2 is t)  # is not iterable


class DictFunctionality(object):
    def __init__(self, values=None):
        if values is None:
            self.values = {}
        elif isinstance(values, dict):
            self.values = values
        else:
            raise ValueError()

    def __str__(self):
        return str(self.values) if self.values else ''

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    # def __contatins__(self, item):
    #       returm item in self.values

    def __len__(self):
        return len(self.values)  # self.values.__len__()


# if __name__ == '__main__'
# l = DictFunctionality({'1key': 'some value'})  # __init__
#  l[1] = 'item1'  # __setitem__
#   print(str(l), l[1])  # __str__, __getitem__
#    for item in l:  # __iter__
#         print(item, l[item])
#     print('s' in l, 1 in l)  # __contains__
#     print(len(l))          # __len__


# Методы, используемые для создания и вызова обьектов
# Методы для работы с атрибутами классов
# Другие
# Документация по всем магическим методам


# is или ==
t = MathObject()
m = MathObject()
t == m
1 == 1
1 is 1

# == - сравнивает по значению
# is - сравнивает по ячейке памяти напрямую. Является ли этот обьект явно этим жe обьектом.
# как посмотреть ячейку памяти?
# id()
# id(x) == id(y) ТО ЖЕ САМОЕ ЧТО И x is y
# Разница между is None и == None
# ...
# 1 == True >> > True
# 1 is True >> > False
# 3 кейса использования is
# 1)Если нужно определить что пришла именно булева переменная True
# 2)Если нужно сравнить по ячейке памяти
# 3)Для Ноне


# Класс - тоже обьект
# Это значит что его можно:
# 1)Напечатать
# 2)Положить в массив
# 3)Сказать что атрибут класса равен чему-то
# 4)Положить в переменную
# 5)Передавать как аргумент
# 6)Принимать как аргумент
# 7)Возвращать в качестве возвращаемого значения

s = []
print(type([]))
print(type(type([])))
print(type(type(type([]))))


class Test(object):
    pass


Test.value = 2
t = Test()
dir(t)
print(t.__class__)
print(type(t))


class MathObject(object):
    pass


MathObject.value = 2
t = MathObject()
print(t.value)

print(t.__class__)
print(t.value == t.__class__.value)

MathObject.value = 2


class MathObject(object):
    value = 2


t = MathObject()
t1 = MathObject()

print(t.value, t.__class__.value)  # >> > 2 2
print(t1.value, t1.__class__.value)  # >> > 2 2

t.value = 10
print(t.value, t.__class__.value)  # >> > 10 2
print(t1.value, t1.__class__.value)  # >> > 2 2

MathObject.value = 5
print(t.value, t.__class__.value)  # >> > 10 5
print(t1.value, t1.__class__.value)  # >> >5 5

# обьект сначала обращается к ближайшему атрибуту. Если у себя не находит, тогда обращается к родителю. Это похоже на MRO, Только для обьектов
# 1)Проверяем в себе
# 2)Если не нашли в себе, то идем в класс. Если там ничего не нашли, то AttributeError


class MathObject(object):
    value = 2

    def __init__(self, i):
        self.value = i


t = MathObject(10)
print(t.value, t.__class__.value)

# Нельзя иметь в одном классе 2 переменные с одинаковым названием. Какие переменные нужно назначать в класс, а какие в инстанс для конкретного экземпляра?
# * 1*Если мы хотим иметь некое значение, уникальное для каждого обьекта, то мы говорим что это инстанс атрибут, который устанавливается через селф в конструкторе
# * 2*Если мы хотим иметь некие значения, единые для всего класса, и более того мы хотим чтобы при изменении этого значения изменились атрибуты всех членов этого класса, то мы использоуем "статическую" переменную внутри класса.


# Статический метод - такой, который можно вызвать от класса, а не от инстанса
class MathObject(object):
    value = 2

    def __init__(self, i):
        self.i = i

    def count(self):
        return 'some'


t = MathObject(10)

# Для того, чтобы сказать что какой то метод является статическим, нужно над ним написать @staticmethod, и убрать из метода self
#
# Поля и методы класса могут быть статическими. Это значит что они принадлежат прямо классу, и поэтому их там можно вызывать и менять.
# Статический метод необходим для того, чтобы вызывать внутри класса какую то логику, которая не зависит от текущего состояния обьекта, и явным образом это показывать
