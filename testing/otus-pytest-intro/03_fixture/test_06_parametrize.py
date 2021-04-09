import pytest
from collections import namedtuple
# https://www.youtube.com/watch?v=OVaKlTR87yk&t=1256s&ab_channel=OTUS%D0%9E%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD-%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5
# 1:15:00

Person = namedtuple('Person', 'name age')

persons = [
    Person('John', 1982),
    Person('Mike', 1998),
]


def id_func(test_data):
    return [f'Person({p.name},{p.age})' for p in test_data]


# @pytest.fixture(params=persons, ids=id_func(persons))
@pytest.fixture(params=persons)
def person(request):
    return request.param


# @pytest.mark.parametrize('a', [1, 2])
# def test_names(person, a):
def test_names(person):
    assert isinstance(person.name, str)
