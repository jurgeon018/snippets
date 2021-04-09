import pytest


@pytest.fixture
def data_1():
    return 1


@pytest.fixture
def print_hello():
    print('hello')


def test_data_1(print_hello):
    pass


def test_data_2(data_2):
    assert data_2 == 2


def test_data_3(data_3):
    assert data_3 == 3
