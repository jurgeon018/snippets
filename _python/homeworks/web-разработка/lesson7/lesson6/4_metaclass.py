# создадим класс "на лету"
MyClass = type('MyClass', (), {})

# можно наследоваться
class MyNewClass(MyClass):
    pass

# добавим атрибутов
MyClass = type('MyClass', (), {'a': 123, 'b': 'string'})

# и методов
def some_method(self):
    return self

MyClass = type('MyClass', (), {'a': 123, 'b': 'string', 'method': some_method})
MyNewClass = type('MyNewClass', (MyClass,), {})

obj = MyNewClass()
print(dir(obj))
print(obj.method())


# в питоне все является объектом
# числа, строки, функции и классы являются объектом и все они были созданы 
# из класса:
age = 35
print(age.__class__) # <type 'int'>
name = 'bob'
print(name.__class__) # <type 'str'>
def foo(): pass
print(foo.__class__) # <type 'function'>
class Bar(object): pass
b = Bar()
print(b.__class__) # <class '__main__.Bar'>

# а сами классы были созданы из type:
print(age.__class__.__class__) # <type 'type'>
print(foo.__class__.__class__) # <type 'type'>
print(b.__class__.__class__)   # <type 'type'>


class MyMetaclass(type):
    # Метод __new__ вызывается перед __init__
    # Этот метод создаёт объект и возвращает его,
    # __init__ просто инициализирует объект, переданный в качестве аргумента.
    # Обычно вы не используете __new__, если только не хотите 
    # проконтролировать, как объект создаётся
    # В данном случае созданный объект это класс, и мы хотим его настроить,
    # поэтому мы перегружаем __new__.

    def __new__(cls, name, bases, dct):
        print("created...")
        if 'a' in dct:
            dct['b'] = 200
        else:
            dct['c'] = 300
        return type.__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMetaclass):
    # во второй версии питона метакласс задавался вот так:
    # __metaclass__ = MyMetaclass
    a = 100

# Можно создать класс и так (по аналогии с type)
MyClass = MyMetaclass('MyClass', (), {'a': 100})

a = MyClass()
print(a.a + a.b)








