##########################################
# 1.Бинарный поиск
from collections import deque


def binary_search(list, item):
    l = 0
    h = len(list) - 1
    counter = 0
    while l <= h:
        counter += 1
        m = (h+l)//2
        guess = list[m]
        if guess == item:
            return m, item, counter
        if guess > item:
            h = m - 1
        if guess < item:
            l = m + 1
    return 'There is no such item in list'


list = [i for i in range(2049)]
# print(binary_search(list,2048))
##########################################

# 2.Сортировка выбором


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = arr[0]
        for i in arr:
            if i < smallest:
                smallest = i
        new_arr.append(arr.pop(arr.index(smallest)))
    return new_arr


l = [5, 3, 6, 2, 10]
# print(selection_sort(l))
##########################################

##########################################
# 3.Рекурсия


def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))


n = 5
fact = 1
for i in range(1, 5):
    fact *= i
##########################################

##########################################
# 4. Разделяй и властвуй
# Упражнение 4.1


def summ1(l):
    total = 0
    for i in l:
        total += i
    return total


def summ2(l):
    if len(l) == 0:
        return 0
    return l.pop(0) + summ2(l)


def summ3(l):
    if l == []:
        return 0
    return l[0] + summ3(l[1:])

# Упражнение 4.2


def count(l):
    if l == []:
        return 0
    return 1 + count(l[1:])
# Упражнение 4.3


def maxx(l):
    if len(l) == 2:
        if l[0] == l[1]:
            return l[0]
        elif l[0] > l[1]:
            return l[0]
        elif l[0] < l[1]:
            return l[1]
    sub_max = maxx(l[1:])
    if l[0] == sub_max:
        return l[0]
    elif l[0] > sub_max:
        return l[0]
    elif l[0] < sub_max:
        return sub_max


l1 = []
l2 = [3]
l3 = [1, 2, 3, 4, 5, 6, 22]
# print(summ3(l3))
# print(count([1,2,3,4,5,6,22]))
# print(maxx([1,2,3,4,33,5,6,22]))

# 4.Быстрая сортировка


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10,66,3,87,234,3,5,7]))
##########################################

##########################################
# 5.Хеш-таблицы

##########################################


##########################################
# 6. Поиск в ширину
graph = {
    "you": ["alice", 'bob', "claire"],
    'bob': ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonnym": []
}


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person[-1] == 'm':
                return person + ' is a mango seller'
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


print(search('you'))
##########################################

##########################################
# 7. Алгоритм дейкстры
graph = {'start': {'a': 6, 'b': 2},
         'a': {'fin': 1},
         'b': {'a': 3, 'fin': 5},
         'fin': {}
         }
costs = {'a': 6,
         'b': 2,
         'fin': float('inf')
         }
parents = {'a': 'start', 'b': 'start', 'in': None}
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    # Перебрать все узлы
    for node in costs:
        # Узел в текущей итерации
        cost = costs[node]
        # Если этот узел имеет наименьшую стоимость, и он еще небыл обработан ...
        if cost < lowest_cost and node not in processed:
            # ... он назначается новым узлом с наименьшей стоимостью
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# Найти узел с наименьшей стоимостью среди необработанных
node = find_lowest_cost_node(costs)
# Пока есть необработанные узлы - цикл продолжается. Если обработаны все узлы - цикл завершен
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    print(node, cost, neighbors)
    # Перебрать всех соседей текущего узла
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Если к соседу можно добраться через текущий узел, то ...
        if costs[n] > new_cost:
            # ... обновить стоимость для этого узла
            costs[n] = new_cost
            # Этот узел становится новым родителем для соседа
            parents[n] = node
    # Узел помечается как обработанный
    processed.append(node)
    # Найти следующий узел для обработки и вернуться в начало цикла с новым значением в переменной node
    node = find_lowest_cost_node(costs)
# print(processed)
##########################################

##########################################
# 8. Жадные алгоритмы

##########################################

##########################################
# 9. Динамическое программирование
##########################################

##########################################
# 10.Алгоритм к-ближайших соседей

##########################################
##########################################
# 11.Бинарное дерево поиска

##########################################
