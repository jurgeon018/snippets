import pytest


@pytest.fixture
def class_fixt():
    print('class_fixt started')


@pytest.mark.usefixtures('class_fixt')
class TestSomething:

    def test_3(self):
        print('test_3 started')

    def test_4(self):
        print('test_4 started')
