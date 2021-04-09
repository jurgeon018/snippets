import pytest


@pytest.fixture(autouse=True)
def auto():
    print('autouse fixture')


def test_01():
    print('test_01 started')
