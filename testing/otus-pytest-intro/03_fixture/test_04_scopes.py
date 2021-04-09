import pytest


'''
pytest 03_fixture/test_04_scopes.y --setup-show
'''


@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def module_scope():
    pass


@pytest.fixture(scope='session')
def session_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass


def test_1(session_scope, module_scope, func_scope):
    pass


def test_2(session_scope, module_scope, func_scope):
    pass


@pytest.mark.usefixtures('class_scope')
class TestSomething:

    def test_3(self):
        pass

    def test_4(self):
        pass
