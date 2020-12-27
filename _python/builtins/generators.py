# Генератор - функция, возвращающая итератор генератора.
import time
from random import *
import sys
from functools import reduce


def generate_random():
    # Нужно написать генератор, который бы каждый раз возвращал случайное значение
    yield random.randint(1, 1000)


# print('random')
# print(next(generate_random()))


def my_range(start, stop, step=1):
    # Нужно написать генератор, который бы работал как range()
    while start < stop:
        yield start
        start += step


# print('range')
# print(list(my_range(50, 100, 4)))
# print(list(range(50, 100, 4)))


def my_enumerate(iter, start=0):
    # Нужно написать генератор, который бы работал как enumerate()
    for i in iter:
        yield start, i
        start += 1


# print('enumerate')
# print(list(my_enumerate('Andrew', 1)))
# print(list(enumerate('Andrew', 1)))


def my_map(func, iterables):
    # Нужно написать генератор, который бы работал как map()
    for i in iterables:
        yield(func(i))

# print('map')
# print(list(my_map(lambda x: x*2, [1, 2, 3, 4, 5, 6, 7, 8])))
# print(list(map(lambda x: x*2, [1, 2, 3, 4, 5, 6, 7, 8])))


def my_reduce(func, array, initial=0):
    for item in array:
        result = func(item)


def fff(x, y):
    print(x)
    print(y)
    return x+y


print(reduce(fff, [1, 2, 3]))


def my_zip(first, second):
    # Нужно написать генератор, который бы работал как zip()
    for i in range(len(first)):
        yield first[i], second[i]


# print('zip')
# print(list(my_zip(['a', 'b', 'c', ], ['1', '2', '3'])))
# print(list(zip(['a', 'b', 'c', ], ['1', '2', '3'])))

######################################################
# Сorey Schafer


def square_numbers(nums):
    for i in nums:
        yield i*i


my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)  # >>> <generator object <genexpr> at >
my_nums = square_numbers([1, 2, 3, 4, 5])
print(next(my_nums))  # >>> 1
print(next(my_nums))  # >>> 2
print(next(my_nums))  # >>> 3
print(next(my_nums))  # >>> 4
print(next(my_nums))  # >>> 5
# print(next(my_nums))  # >>> StopiterationError

for num in my_nums:
    print(num)  # >>> 1\n 2\n 3\n 4\n 5\n


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business', 'Music', ]


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': choice(names),
            'major': choice(majors)
        }
        result.append(person)


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': choice(names),
            'major': choice(majors)
        }
        yield person


t1 = time.clock()
people = people_list(10**6)
t2 = time.clock()
print(t2-t1)

t1 = time.clock()
people = people_generator(10**6)
t2 = time.clock()
print(t2-t1)
