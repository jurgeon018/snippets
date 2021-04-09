from math import sqrt

TYPE_ERROR_TEXT = 'Not valid type for param'


def add(a, b):
    return a + b


def square_equation_solver(a, b, c):
    # v1
    if not all(
        map(
            lambda p: isinstance(p, (int, float)),
            (a, b, c),
        )
    ):
        raise TypeError(TYPE_ERROR_TEXT)
    # # v2
    # for param in (a, b, c):
    #     if not isinstance(param, (int, float)):
    #         raise TypeError(TYP)
    print('Types are ok')

    if a == 0:
        if b == 0:
            return None, None
        return -c / b, None
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    d_root = sqrt(d)
    divider = 2 * a
    x1 = (-b + d_root) / divider
    x2 = (-b - d_root) / divider
    if d == 0:
        x2 = None
    elif x2 > x1:
        x1, x2 = x2, x1
    return x1, x2
