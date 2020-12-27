# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов:
# know(person), который позволяет добавить другого человека в список знакомых.
# is_known(person), который возвращает знакомы ли два человека


class Person:
    age = None
    name = None

    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.known_persons = []

    def know(self, person):
        if person not in self.known_persons:
            self.known_persons.append(person)
            print(f'Now {self.name} knows {person.name}')
        else:
            print(f'{self.name} already know {person.name}')

    def is_known(self, person):
        if person not in self.known_persons:
            print(f'{self.name} dont know {person.name}')
        else:
            print(f'{self.name} know {person.name}')


petro = Person('Petro', 33)
ksu = Person('Ksu', 22)
petro.is_known(ksu)
petro.know(ksu)
petro.is_known(ksu)
petro.know(ksu)
ksu.is_known(petro)
ksu.know(petro)
ksu.is_known(petro)
ksu.know(petro)
# *ЗАДАЧА 2:
# Есть класс Printer, который выводит информацию в консоль.
# У него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию,
# окружая ее строками из *


class Printer(object):
    def log(self, *values):
        return(values)


class FormattedPrinter(object):
    def wrapper(self, value):
        print("***************")
        print(value)
        print("***************")


obj1 = Printer()
obj2 = FormattedPrinter()
obj2.wrapper(obj1.log('bla bla bla', 'hehehey!', "скибидик пук пэй"))


# *ЗАДАЧА 3:
# Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны
# для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)
class Animal(object):
    def __init__(self, name):
        self.name = name


class Human(object):
    def __init__(self):
        self.dangerous = ['lion', 'tiger', 'snake',
                          'crocodile', 'dragon', 'wolf', 'bear', 'shark', ]
        self.not_dangerous = ['cat', 'dog', 'parrot',
                              'elephant', 'owl', 'squirrel', 'turtle', 'dear', 'cow']

    def is_dangerous(self, animal):
        if animal in self.dangerous:
            print('{} is dangerous for human'.format(animal))
        elif animal in self.not_dangerous:
            print('{} is not dangerous for human'.format(animal))
        else:
            print('Current animal({}) is not defined'.format(animal.name))


animal = Animal('cow')
human = Human()
human.is_dangerous(animal.name)


# ЗАДАЧА 4:
# 1.Создать класс корзина, у которого можно выставить разную вместительность для разных обьектов. В обьекты класса корзина можно помещать разные обьекты.
class Basket(object):
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.storage = {}

    def put(self, thing):
        self.current_capacity += thing.size
        if self.max_capacity < self.current_capacity:
            print(f'Capacity of {self.__class__.__name__} is too low')
        else:
            self.storage[thing.name] = thing.size

    def show_content(self):
        print(self.storage)
# 2.Создать класс пакет, у которого можно выставить разную вместительность для разных обьектов. В обьекты класса пакет можно помещать разные обьекты.


class Package(Basket):
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.storage = {}

# 3.Создать любой класс, обьекты которого можно помещать в корзину и в пакет.


class Any(object):
    def __init__(self, name,  size):
        self.name = name
        self.size = size


# 4.Если вместимость пакета или корзины недостаточная, то сказать что обьект поместить нельзя. Понадобятся наследование, конструкторы и методы.
bucket1 = Basket(30)

knife = Any('knife', 10)
toy = Any('toy', 20)
sword = Any('sword', 30)

bucket1.show_content()
bucket1.put(toy)
bucket1.show_content()
bucket1.put(knife)
bucket1.show_content()
bucket1.put(sword)
bucket1.show_content()

package1 = Package(30)
package1.show_content()
package1.put(toy)
package1.show_content()
package1.put(knife)
package1.show_content()
package1.put(sword)
package1.show_content()
