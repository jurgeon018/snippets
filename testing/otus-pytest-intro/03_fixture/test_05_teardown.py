import pytest


@pytest.fixture
def fixt(request):
    print('begin in fixt')
    print(f'call from {request.function.__name__}')
    yield
    print('rolling back in fixt')


@pytest.fixture
def fixt_fin(request):
    print('begin in fixt_fin')
    print(f'call from {request.function.__name__}')

    def fin():
        print('rolling back in fixt_fin')

    request.addfinalizer(fin)


def test_01(fixt):
    print('test_01 started')
