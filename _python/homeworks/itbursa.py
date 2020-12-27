# _________________________________________________________________________
# 1.1. Реверсировать строку original_string.
# original_string = "ambulance"
# reverse_string = "ecnalubma"
from datetime import datetime, date
import csv
import datetime
original_string = "ambulance"
print(''.join([i for i in reversed(original_string)]))
# reverse_string = original_string[::-1]
# print(reverse_string)
# ____________________________________________________________________
# 1.2. Вывести каждый третий символ.
# original_string = '123456 7 890 abc'
# change_string = '36 0b'
original_string = '123456 7 890 abc'
change_string = original_string[2::3]
print(change_string)
# ____________________________________________________________________
# 1.3. Подсчет гласных букв в строке var_string.Программа должна быть нечувствительна к регистру.
# var_string = "hApPyHalLOweEn!"
# counting_vowels = 5
var_string = "hApPyHalLOweEn!"
counting_vowels = 0
for i in var_string:
    if i.lower() in 'aeiou':
        counting_vowels += 1
print(counting_vowels)
# ____________________________________________________________________
# 1.4. Подсчет количества вхождений подстроки "wow" в строке var_string.
var_string = "wowhatamanwowowpalehche"
count = 0
for i in range(len(var_string)):
    if var_string[i:i+3] == 'wow':
        count += 1
print(count)
# _________________________________________________________________________
# 2.1. найти в строке text слова палиндромы (слова, читающиеся одинаково в обоих направлениях) и вывести на печать количество найденых слов.
# в строке могут быть знаки припинания , . : ; ! ? которые не должны влиять на результат
# регистр в слове не имеет значения слово "sos" и "Sos" считается палиндромом.
# text = "Swedish pop group ABBA, single SOS unique occo both palindromes."
# palindromes = 4
text = "Swedish pop group ABBA, single SOS unique occo both palindromes."
palindromes = 0
for i in text.split():
    word = i.lower().rstrip(',.:;!?')
    if word == word[::-1]:
        palindromes += 1
print(palindromes)
# ____________________________________________________________________
# 2.2. Модифицироватьстроку var_string так: в начале строки идут нечетные числа в порядке возрастания. Далее идут четные числа в порядке убывания
# var_string = '1486371'
# change_string = '1137864'
var_string = '1486529371'
odd, even = [], []
for i in var_string:
    if int(i) % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
# odd = filter(lambda x: int(x) % 2 == 1, list(var_string))
# even = filter(lambda x: int(x) % 2 == 0, list(var_string))
change_string = ''.join(sorted(odd)+sorted(even, reverse=True))
print(change_string)
# ____________________________________________________________________
# 2.3. Найти в строке var_string подстроку максимальной длинны, упорядоченною в алфавитном порядке. Если длины строк совпадают печатаем первую найденную.
# var_string = "sabrrtuwacaddabra"
# longest = "abrrtuw"
var_string = "sabrrtuwacaddabra"


def longest(var_string):
    longest = []
    for i in range(len(var_string)-1):
        if var_string[i] <= var_string[i+1]:
            longest.append(var_string[i])
    return ''.join(longest)


def longest2(var_string):
    longest = ''
    if var_string:
        curString = var_string[0]
        longest = var_string[0]
        for i in range(1, len(var_string)):
            if var_string[i] >= curString[-1]:
                curString += var_string[i]
                if len(curString) > len(longest):
                    longest = curString
            else:
                curString = var_string[i]
    return(longest)


print(longest(var_string))
print(longest2(var_string))

# ____________________________________________________________________
# 3.1
# Функция func(a, b) анализирует переменные (a и b могут быть типа "str" или "int") и возвращает:
# - "str" - если хотя бы одна из переменных является строкой;
# - ">" - если var_a больше var_b;
# - "=" - если значения переменных равны;
# - "<" - если var_a меньше var_b.
# Вызов функции: func(5, '2')
# Возвращает: 'str'


def func(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return 'str'
    elif a > b:
        return '>'
    elif a == b:
        return '='
    elif a < b:
        return '<'


print(func(5, "2"))
# ____________________________________________________________________
# 3.2
# Создать функцию count_holes(value), которая принимает аргумент value - целое число или строка содержащая целое число.
# Функция возвращает целое число - количество "отверстий"  в записи этого числа, или строку 'error', если переданый аргумент не удовлетворяет требованиям: число не целое или вообще не является числом. Нули в начале записи числа не учитывать, если таковые имеются.
# Вызов функции: count_holes('08824')
# Возвращает: 5


def count_holes(value):
    count = 0
    if isinstance(value, float):
        return 'error'
    try:
        value = int(value)
    except ValueError:
        return 'error'
    for i in str(value):
        if str(i) in '469':
            count += 1
        elif str(i) in '8':
            count += 2
    return count


print(count_holes('8824'))
# ____________________________________________________________________
# 3.3. word - строка и letters - список букв.
# Заменить буквы в строке word на _, если их нет в списке letters
# Вызов функции: hangman('python', ['a', 'r', 'y', 'i', 'o'])
# Возвращает: '_ y _ _ o _'


def hangman(word, letters):
    # result = []
    result = ''
    for letter in word:
        if letter in letters:
            # result.append(letter)
            result += letter
        elif letter not in letters:
            # result.append(' _ ')
            result += ' _ '
    return result
    # return ''.join(result)


print(hangman('python', ['a', 'r', 'y', 'i', 'o']))
# ___________________________________________________________________________
# 4.1#
# Функция принимает кортеж любых чисел или строк и модифицирует его в кортеж кортежей по два элемента (парами).
# Пример
# Вызов функции: double_tuple((1,4,8,6,3,7,1))
# Возвращает: ((1,4),(8,6),(3,7),(1,))


def double_tuple(value):
    result = []
    for i, item in enumerate(value):
        if i % 2 == 0:
            result.append((value[i:i+2]))
    return tuple(result)


print(double_tuple((1, 4, 8, 6, 3, 7, 1)))
# ____________________________________________________________________
# 4.2#
# Дан текст text и ограничение длины текста limit (в количестве символов). Необходимо, создать функцию trimmed_text(text, limit), которая в случае, если текст не помещается в ограничение обрезает его, но при этом слова не должны обрываться на середине (исключение первое слово), и в конце нужно добавить троеточие ("..."). Перед троеточием не должно быть других разделительных знаков
# Пример
# Вызов функции: trimmed_text("Proin eget tortor risus.", 24)
# Возвращает: "Proin eget tortor risus."
# Вызов функции: trimmed_text("Proin eget tortor risus.", 23)
# Возвращает: "Proin eget tortor..."
# Вызов функции: trimmed_text("Proin eget tortor risus.", 6)
# Возвращает: "Pro..."


def trimmed_text(text, limit):
    new_text = text.split()
    if len(text) < limit:
        return text
    while len(new_text) < limit:
        new_text.pop()
        if len(' '.join(new_text)) < limit:
            return ' '.join(new_text) + '...'


def trimmed_text2(text, limit):
    if len(text) <= limit:
        return text
    elif limit < len(text):
        index = text.rfind(' ', 0, (limit - 2))
        if index == -1:
            index = limit - len("...")
        return text[:index].rstrip(',.:;!?') + "..."


print(trimmed_text("Proin eget tortor risus.", 7))
print(trimmed_text("Proin eget tortor risus.", 24))
print(trimmed_text2("Proin eget tortor risus.", 7))
print(trimmed_text2("Proin eget tortor risus.", 24))
# ____________________________________________________________________
# 4.3#
# Дан текст text, который может содержать буквы латинского алфавита, пробелы и знаки препинания , . : ; ! ?. Необходимо, создать функцию find_most_frequent(text), которая возвращает список слов в нижнем регистре, наиболее часто встречающиеся в тексте, в алфавитном порядке.
# Примечание регистр в словах не имеет значения слова "hello" и "Hello" считаются одним словом.
# Пример
# Вызов функции: find_most_frequent('Hello, hello, my dear!')
# Возвращает: ['hello']
# Вызов функции: find_most_frequent('to understand recursion you need first to understand recursion...')
# Возвращает: ['recursion', 'to', 'understand']


def find_most_frequent(text):
    ntext = ''
    for symbol in text:
        if symbol.lower() in 'qwertyuiopasdfghjklzxcvbnm ':
            ntext += symbol
    words = ntext.lower().split()
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency.update({word: 1})
        elif word in frequency:
            frequency[word] += 1
    for k, v in frequency.items():
        max_key = 'sdfsdf'
        return sorted(frequency)


def find_most_frequent2(text):
    text = text.lower()
    words = text.lower().split()
    clean_words = [word.rstrip(',.:;!?') for word in words]
    frequent_words = []
    max_count_of_occurrences = 0
    for word in set(clean_words):
        count_of_occurrences = clean_words.count(word)
        if count_of_occurrences > max_count_of_occurrences:
            max_count_of_occurrences = count_of_occurrences
            frequent_words = [word]
        elif count_of_occurrences == max_count_of_occurrences:
            frequent_words.append(word)
    frequent_words.sort()
    return frequent_words


print(find_most_frequent('Hello, hello, my dear!'))
print(find_most_frequent('to understand recursion you need first to understand recursion...'))
print(find_most_frequent2('Hello, hello, my dear!'))
print(find_most_frequent2('to understand recursion you need first to understand recursion...'))
# _______________________________________________________________
# 5.1. Kласс Person, отображает запись в книге контактов


class Person:
        # Имеет 4 атрибута: surname - строка, фамилия контакта, first_name - строка, имя контакта, nickname - строка, псевдоним (необязательный, если не задан тогда равен surname), birth_date - объект datetime.date, дата рождения контакта при инициализации передается строкой в формате "YYYY-MM-DD")
    def __init__(self, surname, firstname, birth_date, nickname=None):
        self.surname = surname
        self.firstname = firstname
        self.nickname = nickname
        self.birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
        if nickname is None:
            self.nickname = self.firstname
        # get_age() - считает возраст контакта в полных годах и возвращает строку вида: "27" (пример вывода).

    def get_age(self):
        return str(int((datetime.date.today() - self.birth_date).days/365.25))
        # get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя) контакта, через пробел

    def get_fullname(self):
        return f'{self.surname} {self.firstname}'


print(datetime.datetime.now())

petroff = Person('Mendela', 'Andrew', "1998-12-14", 'jurgeon018')
(petroff.surname)
print(petroff.firstname)
print(petroff.nickname)
print(petroff.birth_date)
print(petroff.get_fullname())
print(petroff.get_age())
# Пример последовательности действий для тестирования класса:
# petroff = Person("Petrov", "Petro", "1952-01-02")
# petroff.surname =>'Petrov'
# petroff.first_name =>'Petro'
# petroff.nickname =>'Petrov'
# petroff.birth_date =>datetime.date(1952, 1, 2)
# petroff.get_fullname() =>'Petrov Petro'
# petroff.get_age() =>'65'
# ____________________________________________________________________
# 5.2.Функция find_oldest_person(filename - путь к файлу csv )создает объекты класса Person, находит старшего по возрасту контакта и возвращает fullname этого контакта.


def find_oldest_person(filename):
    with open(filename, 'r'):
        pass

# Пример csv файла
# surname,name,birthdate,nickname
# Petrov,Petro,1952-01-02,petpet
# Ivanov,Ivan,2000-10-20,
# Sidorov,Semen,1980-12-31,Senya
# Пpимер
# Вызов функции: find_oldest_person('person.csv')
# Возвращает: 'Petrov Petro'
# __________________________________________________________________
# 6.1


class Student:
    # При инициализации объекта, передаются:name - имя студента, строка, conf - настройка для практических работ, словарь в формате, conf = { "lab_max": 10, # количество баллов, доступных за выполнение одной практической работы"lab_num": 7 # количество практических работ}.
    # Экземпляр класса имеет атрибуты:
    # name - строка, имя студента
    # conf #lab_max, lab_num
    # labs - список баллов по практическим работам, количество элементов соответствует lab_num
    def __init__(self, name, conf):
        self.name = name
        self.lab_max = conf['lab_max']
        self.lab_nums = conf['lab_nums']
        self.labs = [0] * self.lab_nums
        # set_lab(self, score, number) сохраняет количество баллов score для практической работы за номером number (практические работы нумеруются от 0 до lab_num-1).
        # При повторной сдаче практической работы засчитывается последнее количество баллов.
        # если number не задан тогда баллы начисляются для первой невыполненной практической (когда балл равен нулю), если таких нет метод возвращает строку 'error'.
        # Если number больше lab_num-1 метод также возвращает строку 'error'.
        # Если score больше lab_max, засчитывается lab_max баллов

    def set_lab(self, score, number):
        pass
        # average_score(self) - возвращает число типа float с округлением до десятых, средний балл по практическим работам. Пример: 4.871 => 4.9

    def average_score(self):
        return round(sum(self.labs))/float(self.lab_nums)


ivan = Student("Ivan", {"lab_max": 5, "lab_nums": 4})
ivan.name
ivan.labs
ivan.set_lab(4, 1)
ivan.labs
ivan.set_lab(5, 2)
ivan.labs
ivan.average_score()
ivan.set_lab(5, 6)
ivan.set_lab(8, 2)
ivan.labs
ivan.set_lab(3, 4)
ivan.labs
ivan.set_lab(5, 3)
ivan.average_score()
# Пример последовательности действий для тестирования класса:
# ivan = Student("Ivan", {"lab_max": 5, "lab_num": 4})
# ivan.name =>'Ivan'
# ivan.labs => [0, 0, 0, 0]
# ivan.set_lab(4, 1)
# ivan.labs => [0, 4, 0, 0]
# ivan.set_lab(5)
# ivan.labs => [5, 4, 0, 0]
# ivan.average_score() => 2.3
# ivan.set_lab(5, 6) => 'error'
# ivan.set_lab(8, 2)
# ivan.labs => [5, 4, 5, 0]
# ivan.set_lab(3)
# ivan.labs => [5, 4, 5, 3]
# ivan.set_lab(5) => 'error'
# ivan.average_score() => 4.3
# ____________________________________________________________________
# 6.2
# Функция find_best_student(filename - путь к файлу csv) создает объекты класса Student, находит студента у которого лучший средний балл по практическим работам и возвращает name этого студента. При этом, вызывать функцию find_best_student() не нужно: система автопроверки вызовет написанную Вами функцию со значением аргумента filename, предопределенным в системе.


def find_best_student(filename):
    with open(filename, 'w'):
        pass
# Пример csv файла, который будет использоваться при вызове функции find_best_student
# name,lab_max,lab_num,l1,l2,l3,l4
# Ivan,10,4,0,2,0,4
# Ira,10,4,10,0,0,0
# Masha,10,4,0,8,8,0
# Sasha,10,4,7,0,3,0
# Пpимер
# Вызов функции: find_best_student('student.csv')
# Возвращает: 'Masha'
# _______________________________________________________________________


# 3

# 5.1


class Person(object):
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        self.nickname = surname if nickname is None else nickname
        date_format = "%Y-%m-%d"
        datetime_object = datetime.strptime(birthdate, date_format)
        self.birth_date = datetime.strptime(birthdate, "%Y-%m-%d").date()

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days / 365.25))

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self.first_name)

# 5.2


def find_oldest_person(filename):
    with open(filename, 'r') as fr:
        reader_dict = csv.DictReader(fr)
        edest_person = None
        for row_dict in reader_dict:
            surname = row_dict['surname']
            name = row_dict['name']
            birthdate = row_dict['birthdate']
            nickname = row_dict['nickname']
            person = Person(surname, name, birthdate, nickname)
            if edest_person is None or int(edest_person.get_age()) < int(person.get_age()):
                edest_person = person
    return edest_person and edest_person.get_fullname()
# 6.1


class Student(object):
    def __init__(self, name, conf):
        self.name = name
        self.lab_max = conf['lab_max']
        self.lab_num = conf['lab_num']
        self.labs = [0] * self.lab_num

    def set_lab(self, score, number=None):
        if number is None and 0 in self.labs:
            number = self.labs.index(0)
        if number is None or number >= self.lab_num:
            return 'error'
        self.labs[number] = score if score <= self.lab_max else self.lab_max

    def average_score(self):
        return round(sum(self.labs) / float(self.lab_num), 1)

# 6.2


def find_best_student(filename):
    with open(filename, 'r') as fr:
        reader_dict = csv.DictReader(fr)
        best_student = None
        for row_dict in reader_dict:
            name = row_dict['name']
            lab_max = int(row_dict['lab_max'])
            lab_num = int(row_dict['lab_num'])
            l1 = int(row_dict['l1'])
            l2 = int(row_dict['l2'])
            l3 = int(row_dict['l3'])
            l4 = int(row_dict['l4'])
            student = Student(name, {'lab_max': lab_max, 'lab_num': lab_num})
            student.set_lab(l1)
            student.set_lab(l2)
            student.set_lab(l3)
            student.set_lab(l4)
            if best_student is None or best_student.average_score() < student.average_score():
                best_student = student
    return best_student.name
