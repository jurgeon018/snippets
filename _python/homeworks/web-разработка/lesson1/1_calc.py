# -*- coding: utf-8 -*-

# =================================
#             Числа
# =================================

print(1+1)
# в python3 синтаксис print(был изменен, теперь это функция)
print(7-3)
print(9/3)
print((60-2*4)/2)
# print(9/0 -> exception)

# операции с целыми числами возвращают целое
print(5/2)

# если одно из чисел с плавающей запятой — результат тоже будет float
print(2.0 / 3) # в python 3 это поведение изменено — операция 2/3 вернет 0.6666666666666666

# целочисленное деление
print(6//5) # вернет 1
print(6.0//5) # вернет float - 1.0
print(7%2) # вернет остаток от деления

print(2 ** 4)
print((2+3j)**2) # комплексные числа

# числа можно округлять по правилам округления:
round(2.1)
round(2.5)
round(2.0/3, 3) # округлим до 3 чисел после запятой

# и брать по модулю:
abs(-2000)


# =================================
#           Переменные
# =================================

x = 10
y = 15
print(x+y)

# X
# Нельзя использовать переменную прежде чем ей будет присвоено значение
# x и X - разные переменные

x += 1 # x = x + 1
print(x)

# Логические операции or, and
x = True
y = False
print(x or y)
print(x and y)

print(False and '77')
print(True and 13)
print(10 and 66)



# =================================
#         Приведение типов
# =================================

# типы можно конвертировать друг в друга
print(float(2))
print(int(11.32), int(12.99)) # вещественное число приводится к целому путем отбрасывания дробной части
print('Prise is: ' + str(11.32) + '$')



# =================================
#             Булевы
# =================================

# Логический тип
# По сути представляет из себя числа 1 и 0
# С некоторыми особенностями отображения на экране:
True
False


# =================================
#              None
# =================================

# Специальный объект None
# Обозначает буквально "ничего"
# Обычно используется для задания начального значения переменным
a = None
# None и False — разные вещи!
print(None == False)





