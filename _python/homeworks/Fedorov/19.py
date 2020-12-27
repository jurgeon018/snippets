# Упражнение 19.1
# Создайте класс Cat. Определите атрибуты name (имя), color (цвет) и weight
# (вес). Добавьте метод под названием meow («мяуканье»). Создайте объект класса Сat,
# установите атрибуты, вызовите метод meow.


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print('meow')


cat1 = Cat('TOmmy', 'grey')
print(cat1.name)
print(cat1.color)
cat1.meow()

# Упражнение 19.2
# 1. Напишите код, описывающий класс Animal:
#  добавьте атрибут имени животного
#  добавьте метод eat(), выводящий «Ням-ням»
#  добавьте методы getName() и setName()
#  добавьте метод makeNoise(), выводящий «Имя животного говорит Гррр»
#  добавьте конструктор классу Animal, выводящий «Родилось животное имя
# животного»
# 2. Основная программа:
#  создайте животное, в момент создания определите его имя
#  узнайте имя животного через вызов метода getName()
#  измените имя животного через вызов метода setName()
#  вызовите eat() и makeNoise() для животного


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Родилось животное {self.name}")

    def eat(self):
        print('Nyam Nyam')

    def getName(self):
        print(self.name)

    def setName(self, name):
        self.name = name

    def makeNoise(self):
        print(f'{self.name} says grrrr')


animal = Animal('Clark')
animal.getName()
animal.setName('Jhon')
animal.getName()
animal.eat()
animal.makeNoise()
# Упражнение 19.3
# Создайте класс StringVar для работы со строковым типом данных, содержащий
# методы set() и get(). Метод set() служит для изменения содержимого строки,
# get() – для получения содержимого строки. Создайте объект типа StringVar и
# протестируйте его методы.


class StringVar:
    def __init__(self, string):
        self.string = string

    def set(self, string):
        self.string = string

    def get(self):
        print(self.string)


string = StringVar('Some Random String')
string.get()
string.set('Changed String')
string.get()

# Упражнение 19.4
# Создайте класс точка Point, позволяющий работать с координатами (x, y).
# Добавьте необходимые методы класса.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_xy(self):
        return self.x, self.y

    def set_xy(self, x, y):
        self.x = x
        self.y = y


point = Point(3, 5)
print(point.get_x())
print(point.get_y())
print(point.get_xy())
point.set_x(22)
point.set_y(3)
point.set_xy(5, 7)
print(point.get_x())
print(point.get_y())
print(point.get_xy())
