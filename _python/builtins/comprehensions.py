#########################################################
# Corey Schafer
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list0 = []
for num in nums:
    if num % 2 == 0:
        my_list0.append(num**2)
my_list1 = [num**2 for num in nums if num % 2 == 0]
# Or with map and lambda:
# my_list = list(map(lambda n: n**2, nums))
# +
# my_list = list(filter(lambda n: n % 2 == 0, nums))
# =
my_list2 = list(filter(lambda n: n % 2 == 0, map(lambda n: n**2, nums)))
# Nested forloops
my_list3 = []
for letter in 'abcd':
    for num in [1, 2, 3]:
        my_list3.append((letter, num))
my_list4 = [(letter, num) for letter in 'abcd' for num in [1, 2, 3]]
# Dict comprehentions
my_dict0 = {}
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
for name, hero in zip(names, heroes):
    if name != 'Peter':
        my_dict0[name] = hero
my_dict1 = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
# Set Comprehentions
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
my_set0 = set()
for n in nums:
    my_set0.add(n)
my_set1 = {n for n in nums}
# Generator Expressions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n**2


my_gen = gen_func(nums)
for i in my_gen:
    print(i)
my_gen = (n**2 for n in nums)
#########################################################
# Олег Молчанов
# (values) = [(expression) for (value) in (collection) if (condition)]
# for (value) in (collection):
#     if (contition):
#         (values).append((expression))

# users = {'John': {'car': 'BMW'}, 'Corey': 'Lambo', 'Mark': 'KIA'}
# cars = [person.get('car', '') for person in users if person.startswith('j')]
# d = {a: a ** 2 for a in range(7)}
# print(cars)
