from random import randint


def attack_damage1(modifier):
    roll = randint(1, 8)
    return modifier + roll


def attack_damage2(modifier):
    roll = randint(1, 8, 'unexpected argument')
    return modifier + roll

