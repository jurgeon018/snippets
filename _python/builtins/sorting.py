# Сортировка списков
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
# >>> [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)  # возвращает None, не меняет список
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]
li.sort()   # возвращает измененый список
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Сортировка кортежей
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# tup.sort()
# >>> AttributeError: 'tuple' object has no attribute 'sort'
s_tup = sorted(tup)
# >>> (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Сортировка словарей
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
# di.sort()
# >>> AttributeError: 'dict' object has no attribute 'sort'
s_di = sorted(di)
# >>> ['age','job','name','os']


# Сортировка по ключу
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
# >>> [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs, reverse=False)
# >>> [1,2,3,-4,-5,-6]


class Employee(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name},{self.age},${self.salary})'


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employees = [e1, e2, e3]
# print(sorted(employees))
# >>>TypeError: '<' not supported between instances of 'Employee' and 'Employee'
print(sorted(employees, key=lambda emp: emp.name))
# >>>[(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]
print(sorted(employees, key=lambda emp: emp.age))
# >>>[(Sarah,29,$80000), (Carl,37,$70000), (John,43,$90000)]
print(sorted(employees, key=lambda emp: emp.salary))
# >>>[(Carl,37,$70000), (Sarah,29,$80000), (John,43,$90000)]
