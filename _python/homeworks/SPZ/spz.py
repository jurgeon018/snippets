# Завдання 1
# 1. Виділити дійсну і уявну частину комплексного числа.
x = complex(1, 2)
x.real
x.imag
# 2. Отримати частку і залишок при діленні цілих чисел.
a, b = 13, 4
a//b
a % b
# 3. Перетворити ціле число у двійкове, вісімкове і шістнадцяткове подання.
a = 100
(a, bin(a), oct(a), hex(a))
# 4. Визначити ідентичність цілого і комплексного числа.
x = complex(3, 4)
y = 5
(id(x), id(y))
# 5. Порівняти об’єкти однакових і різних типів.
type('hello') == type(4)
type([]) == type({})
# 6. Знайти корені квадратного рівняння 5x 2 + 17x +13=0 .
# 7. Обчислити значення математичних функції sin(х) , cos(х) для x =0:90:1.
#
#
#
#
#
# Завдання2
# 1. Написати програму яка вводить довільну стрічку з консолі, підраховує кількість
# повторень кожної букви і виводить результат на екран.2. Написати програму, яка вводить довільне речення з консолі, виділяє слова і поміщає їх
# у список. Відсортований список виводить на екран.
# 3. Задано список, елементами якого є стрічки з суміші чисел і алфавітних символів.
# Використати функція filter() для очищення елементів списку від чисел. Результат вивести на
# екран.
# 4. Задано словник
# ENG_UKR = {"zero":"нуль",
# 	"one":"один",
# 	"two":"два",
# 	"three":"три",
# 	"four":"чотири", "five":"п’ять", "six":"шість", "seven":"сім", 		"eight":"вісім",
# 	"nine":"дев’ять"}
# Написати програму, яка вводить з консолі ( eng = input("number:\n") ) число на
# англійській мові, а виводить на українській, використовуючи словник.
#
#
#
#
#
#
#
#
# Завдання 3
# 1. Написати програму яка в циклі вводить числа з клавіатури. При введенні символу ‘p’ виводить список введених чисел, їхню суму, найменше і найбільше число, середнє значення всіх чисел, при введенні символу ‘q’ завершує програму.
#
# 2. Файли Math.txt, Fiz.txt, Prog.txt містять оцінки студентів з дисциплін Математика, Фізика, Програмування і мають наступну структуру:
# №       Учень	       Оцінка
#     1. Іваненко_І._І. 	5
#     2. Пертренко_П._П. 	4
#     3. Федоренко_.Ф._Ф  	3
# Написати програму, яка читає ці файли і створює один файл All.txt з наступною структурою:
# №      Учень              Математика	Фізика		Програмування
# 1. Іваненко_І._І. 	 5		     5			5
# 2. Пертренко_П._П. 	 4		     4			4
# 3. Федоренко_.Ф._Ф  	 3		     3			3
#
# 3. Написати функцію яка зчитує файл secret.py і перевіряє збалансованість дужок (), [].
#
# 4.Написати програму яка, друкує значення високосних років починаючи з 2000 року. Значення таких років ділиться на 4 без залишку, крім тих, що діляться без залишку на 100 і не діляться  на 400.
#
# 5. Написати програму, яка зчитує з консолі ім’я файлу з Python програмою. Використати блок try/else для оброблення винятку відсутності файлу. При наявності файлу програма читає цей файл, створює словник, де ключами є символи англійської абетки, а значеннями – частота їхнього використання у тексті. В кінці, програма виводить відсортований словник символів абетки за частотою їхнього використання.
#
#
#
#
#
#
# Завдання 4.
# 1. Написати функцію, яка знаходить мінімальне і максимальне значення із довільного
# числа аргументів довільного типу і повертає їх як кортеж. Всі аргументи зібрати у кортеж
# інструкцією * і виконати їх обхід за допомогою простого циклу for .
# 2. Написати функцію, яка повертає перетин (спільні елементи) довільного числа
# послідовностей. Використати кортеж для передачі довільного числа аргументів у функцію.
# Кортеж обробити у простому циклі for .
# 3. Написати програму, яка з консолі вводить ім’я файлу, читає цей файл і записує його в
# новий файл без символів “white space” ( пропуск, \n, \r, \f, \t, \v).
# 4. Написати програму яка виводить перенумерований список всіх файлів поточного
# каталогу згідно заданого розширення. Розширення файлів ввести з консолі.
# 5. Написати програму, яка генерує просту html -сторінку використовуючи шаблон і метод
# str.format() . В шаблоні поля для заміщень вказані у фігурних дужках {name} . Сторінку
# згенерувати виразом tml=HTML_TEMPLATE.format(name1=input1, name2=input2,...) і записати
# у файл. Значення аргументів input1, inout2,... прочитати з файлу param.txt .
# Шаблон має наступний вид:
# HTML_TEMPLATE = """<?xml version="1.0"?>
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" \
# "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
# <html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head>
# <title>{title}</title>
# <!-- {copyright} -->
# <meta name="Description" content="{description}" />
# <meta name="Keywords" content="{keywords}" />
# <meta equiv="content-type" content="text/html; charset=utf-8" />
# {stylesheet}\
# </head>
# <body>
# {boby_text}
# </body>
# </html>
# """
#
#
#
#
# Завдання 5
# 1.Задано модуль point.py з класом Point :
# # Модуль poin.py
# """
# Цей модуль забезпечує клас Point
# >>> point = Point()
# >>> point
# Point(0, 0)
# >>> point.x = 12
# >>> str(point)
# '(12, 0)'
# >>> a = Point(3, 4)
# >>> b = Point(3, 4)
# >>> a == b
# True
# >>> a == point
# False
# >>> a != point
# True
# """
# import math
# class Point:
# def __init__(self, x=0, y=0):
# """2D картезіанські координати
# > point = Point()
# > point
# Point(0, 0)"""
# self.x = x
# self.y = y
# def distance_from_origin(self):
# """Повернення віддалі від точки до початку координат
# > point = Point(3, 4)
# > point.distance_from_origin()
# 5.0
# """
# return math.hypot(self.x, self.y)
# def __eq__(self, other):
# return self.x == other.x and self.y == other.y
# def __repr__(self):
# return "Point({0.x!r}, {0.y!r})".format(self)
# def __str__(self):
# return "({0.x!r}, {0.y!r})".format(self)
# if __name__ == "__main__":
# import doctest
# doctest.testmod()
# Змінити клас Point так, щоб забезпечити підтримку наступних операцій, де p, q, r є
# об'єктами типу Point , а n - число. Розширити doctest для перевірки зміненого класу.
# p=q+r
# p+=q
# p=q-r
# p=-q
# p=q*n
# p*=n
# p=q/n
# p/=n
# p=q//n
# p//=n
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# Point.__add__()
# Point.__iadd__()
# Point.__sub__()
# Point.__isub__()
# Point.__mull__()
# Point.__imull__()
# Point.__truediv__()
# Point.__itruediv__()
# Point.__floordiv__()
# Point.__ifloordiv__()
# 2. Написати клас Rectungle , який успадковує клас Point . Добавити в похідному класі
# методи для обчислення периметру і площі квадрату за заданими чотирма точками.
#
#
#
#
#
#
# Завдання 6
# . Написати сценарій, який продивляється список аргументів командного рядка, шукає
# пари -name value і поміщує їх у словник парами ключ:значення ( name: value ).
# 2. Написати сценарій, який за заданим ім’ям файлу з консолі, читає цей файл,
# перенумеровує всі рядки, за винятком рядків коментарів, і перенумерований файл записує в
# інший файл.
# 3. Написати сценарій, який друкує поштовий конверт з використанням шаблонного тексту
# з іменами змінних. Адреси відправника і приймача читаються з двох окремих файлів.
# 4. Написати сценарій, який виводить послідовність із 10 чисел Фібоначі викликаючи
# функцію-генератор.
# 5. Написати сценарій, який зчитує ім’я конфігураційного файлу, заданого у командному
# рядку, відкриває і читає рядки конфігураційного файлу виду name = value у словник як
# name:value . Отриманий словник спочатку архівується, а потім розархівовується з
# використанням модуля pickle у новий файл.
#
#
#
#
#
#
#
# Завдання 7
# 1. Написати програму, яка перекодовує текст з набором символів Windows cp1252 у набір
# символів UTF-8 .
# 2. Написати програму, яка перетворює символьний рядок “Привіт учасникам олімпіади” з
# типом символів str в послідовність змінюваних байтів типу bytearray . У цій послідовності
# збільшити значення байтів на 1 і записати назад у символьний рядок. Значення символьного
# рядка до і після зміни вивести на екран.
# 3. Написати програму, яка використовує модуль re і шаблони для пошуку в тексті адреси
# електронної пошти user@pu.if.ua і номерів телефонів +380 dd ddd dddd (де d люба десяткова
# цифра) і друкує їх на консоль
# 4. Написати програму з використанням шаблонів, які замінює дати в європейському
# форматі на звичайний формат, наприклад 10/05/25 на 10 травня 2025 року.
# 5. Виконати завдання 2 з використанням модуля struct .
#
#
#
# Завдання 8
# . Написати програму, яка порівнює два каталоги і виводить списки однакових файлів і
# файлів з однаковим змістом.
# 2. Написати програму, яка виводить список імен файлів, які співпадають із шаблоном.
# Шаблон ввести як параметр командного рядка.
# 3. Написати програму яка копіює файл або каталог із src у dst . Значення src і dst ввести
# як параметр командного рядка. Програма має перевірити існування файлів або каталогів з
# іменами src і dst .
# 4. Написати дві програми, які обмінюються повідомленнями через відображення файлів у
# пам'ять. Отримані повідомлення вивести на екран і після цього завершити роботу програм.
# 5. Написати дві програми, які обмінюються повідомленнями через іменований канал.
# Отримані повідомлення вивести на екран і після цього завершити роботу програм.
#
#
#
# Завдання 9
# 1. Написати програму, яки перед завершенням видає повідомдення “Допобачення”.
# 2. Написати програму в якій для простого класу створюється декілька екземплярів obj1,
# ojb2, obj3. Вивести список об’єктів, які які безпосередньо посилаються на об’єкти obj1,
# obj2, obj3. Вивести список об’єктів на які посилаються на об’єкти obj1, obj2, obj3.
# 3. Написати програму яка серіалізує і відновлює екземпляри класу.
# 4. Написати програму яка виводить трасувальну інформацію для винятку, спричиненого
# діленням на нуль.
# 5. Написати програму, яка використовує кеш для недавно обчислених арифметичних
# виразів і виводить повідомлення про використання кешу.
#
#
#
# Завдання 10
# 1. Написати програму, яка читає файл з параметрами налаштування для структури
# struct addr {
# char name[32];
# char street[40];
# char city[20];
# int code;
# };
# 2. Написати програму, яка виводить поточну дату, локальний час і час за Гринвічем
# 3. Написати програму в якій виконується операція блокування над одним файлом при його
# записуванні і читанні.
# 4. Написати програму, яка читає з тестового файлу кожний 10-й символ.
# 5. Написати програму, яка відображає файл у пам'ять і використовуючи індексний доступ
# обнуляє значення комірок, індекси яких без залишку діляться на 5. Після закриття
# відображення вивести значення файлу.
#
#
#
# Завдання 11
# 1. Написати програму, яка використовує модуль multiprocessing, для обміну
# повідомленнями між двома процесами з використанням каналу.
# 2. Написати програму, яка використовує клас Queue для обміну повідомленнями між
# двома процесами з використанням черги.
# 3. Написати програму, яка використовує модуль threading для створення і запуску
# функції в окремих потоках.
