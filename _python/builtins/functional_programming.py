from functools import reduce

# map - выполняет какую то функцию для каждого обьекта из массива входных параметров

(list(map(lambda x: len(x), 'How long are the words in this phrase'.split())))

m1 = map(lambda x: x*2, [1, 2, 10])
print(list(m1))

x = [ord(i) for i in 'helloworld']
x = list(map(ord, 'helloworld'))

# filter - оставляет из массива только то, что удовлетворяет условию. Pезультат - новая коллекция. Все данные создаются заново, со старыми ничего не происходит.

f = filter(lambda x: x > 3, [1, 2, 3, 4, 5])
f = filter(lambda x: x != 'todelete', [1, 2, 3, 4, 'todelete', 5])

# reduce - выполняет функцию для каждого объекта из массива входных параметров, а потом оперирует остатком
# Если нужно сложить или умножить все числа в массиве - нужен reduce

r = reduce(lambda x, y: x+y, [1, 2, 3, 4])
print(reduce(lambda x, y: x*10 + y, [3,4,4,2,1]))

# map - исполняет функцию над каждым отдельно
# reduce - исполняет функцию над всеми вместе
# filter - исполняет условие для всех, оставляет только подходящие условию

#################################
l = ['one', 'two', 'three']


new_list = list(map(lambda s: s.upper(), l))
print(new_list)
new_list = [s.upper() for s in l]
print(new_list)

############################


def has_o(string):
    return 'o' in string.lower()


nl = list(filter(has_o, l))

new_l = list(filter(lambda s: 'o' in string.lower(), l))

nl2 = [string for string in l if has_o(string)]

print(nl, new_l, nl2)
