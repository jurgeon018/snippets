from contextlib import contextmanager
import os
##############################################################
# Репликация функции open() при помощи класса


class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with OpenFile('filename.txt', 'w') as f:
    f.write('testing class')

print(f.closed)

##############################################################
# Репликация функции open() при помощи функции и декоратора
@contextmanager
def open_file():
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open('filename.txt', 'w') as f:
    f.write('testing function')

print(f.closed)

##############################################################
# Реальный пример, который позволяет сократить код


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('modules'):
    print(os.listdir())

with change_dir('builtins'):
    print(os.listdir())

with change_dir('algorythms'):
    print(os.listdir())


cwd = os.getcwd()
os.chdir('molchanov')
print(os.listdir())
os.chdir(cwd)


cwd = os.getcwd()
os.chdir('my_excercises')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('algorithms')
print(os.listdir())
os.chdir(cwd)
##############################################################
# Tceh
# Репликация функции open() при помощи класса
class File(object):
    def __init__(self, filename, mode):
        print('__init__')
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('opening file')
        try:
            self.open_file = open(self.filename, self.mode)
        except Exception as e:
            print("Exception in context manager")
            self.open_file = None

        return self.open_file

    def __exit__(self, *args):
        print('closing file')
        if self.open_file is not None:
            self.open_file.close()


#
# with File('to_open.txt', 'w') as f:
#     print('SOME WORK HERE')
#     f.write('some data')

# Note how error is handled:

with File('does-not-exist', 'r') as new_file:
    if new_file is not None:
        print(new_file.read())




# Репликация функции open() при помощи функции и декоратора
from contextlib import contextmanager


@contextmanager
def do_work(value, mode='r'):
    print('some work before, __enter__')
    try:
        open_file = open(value, mode)
    except Exception as e:
        print('Exception was here!')
        #yield None
    else:
        #yield open_file
        open_file.close()
    print('some work after, __exit__')


with do_work('to_open.txt'):
    print('Some work here!')
    # if w is not None:
    #     print(w.read())


def foo():
    # SOME WORK // OPEN FILE
    return open_file
    # SOME WORK AFTER

def gen():
    print('before')
    yield 1
    print('after')
    # yield 2

g = gen()
next(g)
next(g)
