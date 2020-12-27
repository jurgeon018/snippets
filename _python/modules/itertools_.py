import itertools

print('1***************')
# комбинации - порядок не имеет значения
for c in itertools.combinations([1, 2, 3], 2):
    print(c)
print('1***************')
# перестановки - порядок имеет значение
for p in itertools.permutations([1, 2, 3], 2):
    print(p)


my_list = [1, 2, 3, 4, 5, 6]
print('2***************')
combinations = itertools.combinations(my_list, 3)
print([result for result in combinations if sum(result) == 10])
print('2***************')
combinations = itertools.combinations(my_list, 3)
print([result for result in combinations if sum(result) == 10])

word = 'sample'
my_letters = 'plmeas'
combinations = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)
print('3***************')
print(list(combinations))  # >>> ('p','l','m','e','a','s')
for с in combinations:
    if ''.join(с) == word:
        print('Match!')
        break
else:
    print('No Match!')  # >>> No Match!
print('3***************')
print(list(permutations))  # >>> Все возможные комбанации символов
for p in permutations:
    if ''.join(p) == word:
        print('Match!')  # >>> Match!
        break
else:
    print('No Match!')
###################################################

zip(itertools.count(start=5, step=2.3), [1, 2, 3, 4, 5])
itertools.zip_longest(range(10), [1, 2, 3, 4, 5])
itertools.cycle(('On', 'Off'))
itertools.repeat(2, times=3)
itertool.startmap(pow, [(0, 2), (1, 2), (2, 2)])
