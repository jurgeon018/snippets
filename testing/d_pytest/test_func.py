import pytest


@pytest.fixture()
def function_fixture():
    print('fixture for each test')
    return 1


@pytest.fixture(scope='module')
def module_fixture():
    print('fuxture for module')
    return 2


@pytest.fixture
def simple_yield_fixture():
   print('setUp part')
   yield 3
   print('tearDown part')


def test_function_fixture(function_fixture):
    assert function_fixture == 1


def test_yield_fixture(simple_yield_fixture):
    assert simple_yield_fixture == 3


@pytest.mark.xfail
def test_some_magic_test():
   ...

    
@pytest.mark.skip
def test_old_functional():
   ...

