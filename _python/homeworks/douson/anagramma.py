from random import *

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = choice(WORDS)
shuffled = [word[randrange(len(word))] for i in range(len(word))]

print('Анаграмма: ', ''.join(shuffled))
guess = input('Угадайте слово: ')
while guess != word:
    print('You are wrong')
    guess = input('Угадайте слово: ')
    if guess == word:
        print('Yes, exactly')
