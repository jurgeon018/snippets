import time
import math


def timer(func):
    def inner():
        t0 = time.time()
        func()
        t1 = time.time()
        print(f'Time required: {t1-t0}')
    return inner


def prime_tester(func):
    def inner():
        for n in range(1, 10):
            print(n, func(n))
    return inner


@timer
@prime_tester
def is_prime_v0(n):
    if n == 1:
        return False
    d = 2
    while d < n:
        if n % d == 0:
            return False
        d += 1
    return True


@timer
@prime_tester
def is_prime_v1(n):
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


@timer
@prime_tester
def is_prime_v2(n):
    if n == 1:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1+max_divisor):
        if n % d == 2:
            return False
    return True


@timer
@prime_tester
def is_prime_v3(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1+max_divisor, 2):
        if n % d == 0:
            return False
    return True


is_prime_v0()
# is_prime_v1()
# is_prime_v2()
# is_prime_v3()
