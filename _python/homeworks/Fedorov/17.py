# Упражнение 17.1
# Напишите программу, проверяющую четность числа, вводимого с клавиатуры. Выполните обработку возможных исключений.

try:
    x = int(input(':'))
except Exception as e:
    print(e)
try:
    if x % 2 == 0:
        print('num is even')
    else:
        print('num is odd')
except Exception as e:
    print(e)

# Упражнение 17.2*
# Напишите программу, которая будет генерировать матрицу из случайных целых чисел. Пользователь может указать число строк и столбцов, а также диапазон целых чисел. Произведите обработку ошибок ввода пользователя.
import random
x = 5
y = 5
n = 9
for i in range(x):
    for j in range(y):
        print(random.randint(1, n), end='  ')
    print(end='\n')
