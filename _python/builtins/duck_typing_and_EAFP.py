

import os


class Duck:
    def quack(self):
        print('quack, quack')

    def fly(self):
        print('flap, flap')


class Person:
    def quack(self):
        print('im quacking like a duck')

    def fly(self):
        print('im flapping my arms')


def quack_and_fly(thing):
    # pythonic way 1
    thing.quack()
    thing.fly()
    # non-pythonic way 1
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('this has to be a Duck!')
    # non-pythonic way 2(LBYL)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
    # Easier to Ask Forgivness than Permission
    # pythonic way 2(EAFP)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

#########################################################

person = {'name': 'Jess', 'age': 23, 'job': 'programmer'}

# LBYL(Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print('Im {name}. Im {age} years old and i am a {job}'.format(**person))
else:
    print('Missing some keys')
# EAFP(Pythonic)
try:
    print('Im {name}. Im {age} years old and i am a {job}'.format(**person))
except KeyError as e:
    print('Missing {} key'.format(e))

#########################################################

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# LBYL(Non-Pythonic)
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exists')

# EAFP(Pythonic)
try:
    print(my_list[5])
except IndexError:
    print('That index does not exists')

#########################################################

my_file = '/tmp/test.txt'

# Race Condition
if os.access(my_file, os.R_OK):
    f = open(my_file)
    with f:
        print(f.read())
else:
    print('File can not be accessed')

# No Race Condition
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())
