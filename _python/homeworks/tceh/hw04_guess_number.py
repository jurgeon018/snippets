# 1.Игра - угадай число
import random


def f4_1():
    number = random.randint(1, 20)
    print(number)
    while True:
        while True:
            try:
                x = int(input(':'))
                break
            except Exception as e:
                print(e)
        if x == number:
            print('Congratz!')
            break
        elif x > number:
            print('number is lesser')
        elif x < number:
            print('number is bigger')


f4_1()
