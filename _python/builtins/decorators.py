#########################################################
# Corey Schafer
from datetime import datetime
import time


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


def timer(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('time for execution: ', t2)
        return result
    return wrapper


@timer
def display_info(name, age):
    print(f'display_info function ran with arguments ({x}, {y})')


display_info(1, 2)

# @decorator_function
@DecoratorClass
def display():
    print('display function ran')


# @decorator_function
# @DecoratorClass
@timer
def display_info(name, age):
    print(f'display_info function ran with arguments ({name}, {age})')


# display = decorator_function(display)
display()
# display_info = decorator_function(display_info)
display_info(1, 2)

#######################################################
# Decorators with arguments


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f'{prefix}: Executed before {original_function.__name__}')
            result = original_function(*args, **kwargs)
            print(f'{prefix}: Executed after {original_function.__name__}')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('PREFIX')
def display_info2(name, age):
    print(f'display_info ran with arguments ({name}, {age})')


display_info2('John', 32)
display_info2('Mark', 22)

#########################################################
# Олег Молчанов


def timeit(arg):
    # print(arg) # >>> 'name'
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@timeit('name')
def func1(n):
    lst = []
    for i in range(n**4):
        if i % 2 == 0:
            lst.append(i)
    return lst


@timeit('name')
def func2(n):
    lst = [i for i in range(n**4) if i % 2 == 0]
    return lst
