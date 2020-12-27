# -= lambda =- 
# анонимные функции (lambda)

def func(x,y,z):
    return x+y+z
print(func(1, 2, 3))

f = lambda x, y, z: x + y + z
print(f(1, 2, 3))

# В lambda-выражениях можно использовать аргументы со значениями по умолчанию:
x = lambda a='fee', b='fie', c='foe': a + b + c
print(x())

# логика выбора внутри lambda-функций
lower = (lambda x, y: x if x < y else y)
print (lower('bb', 'aa'))


# -= map =-
# Отображение функций на последовательности: map

# увеличить каждый член последовательности на 10
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10) # Прибавить 10 к каждому элементу
print(updated) # [11, 12, 13, 14]

# можно записать короче
def inc(x): return x + 10 # Функция, которая должна быть вызвана
print (list(map(inc, counters))) # Сбор результатов [11, 12, 13, 14]

# и совсем коротко
print(list(map((lambda x: x + 10), counters))) # Выражение-функция [4, 5, 6, 7]


# Обработка списка "сырых строк"
strings = ['   is  ', ' there    ', '  any  ', ' body   ']
strings = list(map(lambda x: x.strip(), strings))
print(strings)
print(' '.join(strings))


a = pow(3, 4) # 3 ** 4
print(a) # 81
b = map(pow, [1, 2, 3], [2, 3, 4]) # 1**2, 2**3, 3**4 # 1**2, 2**3, 3**4 
print(list(b)) # [1, 8, 81]


# -= filter =- 

l1 = list(range(-5, 5)) # Итератор в Python 3.0 
print(l1) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

l2 = filter((lambda x: x > 0), range(-5, 5)) # Итератор в Python 3.0 
print(list(l2)) # [1, 2, 3, 4]


# -= reduce =-

from functools import reduce # В 3.0 требуется выполнить импортирование

a1 = reduce((lambda x, y: x + y), [1, 2, 3, 4]) 
print(a1) # 10

a2 = reduce((lambda x, y: x * y), [1, 2, 3, 4]) 
print(a2) # 24


# -= zip =-

a = [1,2,3,4,5]
b = ['a','b','c']
print(list(zip(a, b))) # [(1, 'a'), (2, 'b'), (3, 'c')]


# -= min, max, sum =-

print(max([1,2,3,4,5])) # 5
print(min([1,2,3,4,5])) # 1
print(sum([1,2,3,4,5])) # 15


