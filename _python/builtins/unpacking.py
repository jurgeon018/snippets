s, k = (1, 2,)  или s, k = [1, 2]
print(s, k) >> > (1, 2)
s, k = (1, 2, 3, 4,) >> > Error
s, k, p = (1, 2) >> > Error

first, *second = 'my string'
print(first, second) >> > m['y', ' ', 's', 't', 'r', 'i', 'n', 'g']

first, *middle, last = 'some letters'
print(first, middle, last) >> > s['o', 'm', 'e', '  ', 'l', 'e', 't', 't', 'e', 'r'] s

# чаще всего используется когда нужно вернуть из функции несколько значений


def func():
    return (1, 10)


x, y = func()
print(x, y) >> > 1, 10


def find_min_max(data):
    min_num = min(data)
    max_num = max(data)
    return min_num, max_num


minimum, maximum = find_min_max([1, 9, 22, -8])

# Распаковка аргументов


def test(x, y, z):
    print(x, y, z)


l = [1, 2, 3]
d = {'x': 1, 'y': 2, 'z': 3}
test(*l)
test(**d)


def gen():
    for i in range(1):
        yield i


print(add(*gen())) -  # не использовать, пототому что генератор не будет отдавать по одному элементу, а за 1 раз раскрутится полностью и может занять очень много памяти
