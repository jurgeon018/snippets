# *ЗАДАЧИ НА ДЕКОРАТОРЫ
from functools import reduce, wraps
import time


# + Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
def canceller(func):
    # @wraps(func)  # используется для сохранения контекста декорируемой функции в декораторе, например для вывода имени декорируемой функции. Если его убрать,то ничего не изменится
    def inner(*args, **kwargs):
        print(f"{func.__name__} is cancelled")
    return inner


# + Реализовать декоратор, который измеряет скорость выполнения функций.
def timer(func):
    # @wraps(func)
    def inner(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time()
        print(f'Time for execution for func {func.__name__}:', t1-t0)
    return inner


# Реализовать декоратор, который будет считать, сколько раз выполнялась функция
def counter(func):
    func.counter = 1

    def inner(*args):
        print(f'Function {func.__name__} runs {func.counter} time')
        func.counter += 1
        return func(*args)
    return inner
# Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение функции, закончено выполнение функции


def logger(func):
    # @wraps(func)
    def inner(*args, **kwargs):
        print('The initial function will execute now.')
        func(*args, **kwargs)
        print('The initial function was executed.')
    print('Finished decorating the initial function.')
    return inner


# + Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать в консоль сообщение об ошибке
def catcher(func):
    # @wraps(func)
    def inner(*args, **kwargs):
        try:
            func(*ags, **kwargs)
        except Exception as err:
            print(f'Exceptrion occured in {func.__name__}. {err}')
    return inner


@canceller
def func1(*args):
    print(f'func1 with args: {args}')


@timer
def func2(*args):
    print(f'func2 with args: {args}')


@counter
def func3(*args):
    print(f'func3 with args: {args}')


@logger
def func4(*args):
    print(f'func4 with args: {args}')


@catcher
def func5(*args):
    print(f'func5 with args: {args}')


print('* ЗАДАЧИ НА ДЕКОРАТОРЫ')
func1(2, 3, 4)
func2(5, 6, 7)
func3(8, 9, 10)
func3(8, 9, 10)
func3(8, 9, 10)
func4(11, 12, 13)
func5(14, 15, 16)

print('*ЗАДАЧИ НА MAP/FILTER/REDUCE (И LAMBDA, ЕСЛИ НУЖНО)')
# + При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
x1 = list(map(lambda x: x % 5, [1, 4, 5, 30, 99]))
print(x1)
# + При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
x2 = list(map(lambda x: str(x), [3, 4, 90, -2]))
print(x2)
# + При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
x3 = list(filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str]))
print(x3)
# + При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
p = list(map(lambda x: len(x), ['some', 'other', 'value']))
x4 = reduce(lambda x, y: x+y, p)
print(x4)
