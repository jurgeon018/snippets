# Упражнение 11.1
import random
L = [3,  3, 3, -5, 4, 3, -1]
if len(L) > 2:
    print(len(L))
    print(abs(min(L) - max(L)))
    if abs(max(L) - min(L)) > 10:
        print(sorted(L))
    else:
        print('difference is less than 10')

# Упражнение 11.2
# L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
# Определите наличие строки «привет» в списке. ЕСЛИ такая строка в списке присутствует, ТО вывести ее на экран, повторив 10 раз.
L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
if 'привет' in L:
    print('привет'*10)
# Упражнение 11.4
# L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
# Определите наличие строки «привет» в списке. ЕСЛИ такая строка в списке
# присутствует, ТО удалить ее из списка, ИНАЧЕ добавить строку в список.
# Подсчитать, сколько раз в списке встречается число 4, ЕСЛИ больше одного раза, ТО
# очистить список.
L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
print(L)
if 'привет' in L:
    L.remove('привет')
else:
    L.append('привет')
print(L)

# Упражнение 11.5
# Напишите программу, которая запрашивает у пользователя две строки и формирует
# из этих строк список. Если строки состоят только из чисел, то программа добавляет в
# середину списка сумму введенных чисел, иначе добавляется строка, образованная из
# слияния двух введенных ранее строк. Итоговая строка выводится на экран.
s1 = input('enter str: ')
s2 = input('enter str: ')
if s1.isalpha and s2.isalpha:
    print(s1+s2)
elif s1.isdigit and s2.isdigit:
    print(s1 + str(int(s1) + int(s2)) + s2)
# Упражнение 11.6
# Задан список слов. Необходимо выбрать из него случайное слово. Из выбранного
# случайного слова случайно выбрать букву и попросить пользователя ее угадать.
# Задан список слов: [ ' самовар ' , ' весна ' , ' лето ' ]
# Выбираем случайное слово: ' весна '
# Выбираем случайную букву: ' с '
# Выводим на экран: ве?на
# Пользователь пытается угадать букву.
# Подсказка: используйте метод choice() модуля random.


words = [' самовар ', ' весна ', ' лето ']
word = random.choice(words)
letter = random.choice(word)


print('Задан список слов: ', words)
print('выбираем случайное слово: ', word)
print('выбираем случайную букву:', '"', letter, '"')
print('выводим на экран:', s)

inp = input('Угадай букву:')
if inp == letter:
    print('Малаца')
else:
    print('Попробуй еще раз')
