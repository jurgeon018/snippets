from functools import lru_cache


def fibonacci_v1(n):
    if type(n) != int or n < 1:
        raise TypeError('n must be a positive int')
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        # print(a)
        yield(a)


def fibonacci_v2(n):
    if type(n) != int or n < 1:
        raise TypeError('n must be a positive int')
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci_v2(n-1) + fibonacci_v2(n-2)


fibonacci_v3_cache = {}


def fibonacci_v3(n):
    if type(n) != int or n < 1:
        raise TypeError('n must be a positive int')
    if n in fibonacci_v3_cache:
        return fibonacci_v3_cache[n]
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_v3(n-1) + fibonacci_v3(n-2)
    fibonacci_v3_cache[n] = value
    return value


@lru_cache(maxsize=1000)
def fibonacci_v4(n):
    if type(n) != int or n < 1:
        raise TypeError('n must be a positive int')
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci_v4(n-1) + fibonacci_v4(n-2)


print(list(fibonacci_v1(16)))
print(list(fibonacci_v2(n) for n in range(1, 17)))
print(list(fibonacci_v3(n) for n in range(1, 17)))
print(list(fibonacci_v4(n) for n in range(1, 17)))
