import pytest


def func(a):
    if a < 0:
        return 'negative'
    elif a == 0:
        return 'zero'
    elif a > 0:
        return 'positive'


def test_negative():
    assert func(-1) == 'negative'


def test_zero():
    assert func(0) == 'zero'


def test_positive():
    assert func(1) == 'positive'


@pytest.mark.parametrize(
    'a, result',
    [
        (-1, 'negative'),
        (0, 'zero'),
        (1, 'positive'),
    ]
)
def test_all_cases(a, result):
    assert func(a) == result


@pytest.mark.parametrize('a', [1, 2])
@pytest.mark.parametrize('b', [3, 4])
def test_intersect(a, b):
    print(a, b)


@pytest.mark.parametrize(
    'a, b',
    [
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4)
    ]
)
def test_intersect2(a, b):
    print(a, b)


