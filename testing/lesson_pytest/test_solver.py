from unittest import TestCase
from solver import add, square_equation_solver, TYPE_ERROR_TEXT
import pytest


class TestAddCase(TestCase):

    def test_ok(self):
        print('test ok 1')
        res = add(1, 2)
        self.assertEqual(res, 3)


class TestSquareEquationSolverUnittest(TestCase):

    def test_raises_type_error(self):
        try:
            square_equation_solver('', 1, 1.5)
        except TypeError as e:
            print(f"OK, error: {e}")
        else:
            # assert False
            self.fail('Did not raise')

    def test_raises_type_error2(self):
        with self.assertRaises(TypeError):
            square_equation_solver('', 1, 1.5)

    def test_result_is_tuple(self):
        res = square_equation_solver(0, 0, 0)
        self.assertIsInstance(res, tuple)

    def test_no_results(self):
        res = square_equation_solver(0, 0, 1)
        self.assertEqual(res, (None, None))

    def test_solves_ok(self):
        res = square_equation_solver(1, -3, -4)
        self.assertEqual(res, (4, -1))

    def function(self):
        pass


@pytest.mark.parametrize(
    'args, expected_result',
    [
        ((1, 2), 3),
        (('foo', "bar"), "foobar"),
    ]
)
def test_add(args, expected_result):
    res = add(*args)
    assert res == expected_result


def test_pytest():
    assert 1 == 1


def test_ok():
    print('test ok 2')
    res = add(1, 2)
    assert res == 3


class TestSquareEquationSolver:
    with pytest.raises(TypeError) as exc_info:
        square_equation_solver('', 1, 1.5)
    assert str(exc_info.value) == TYPE_ERROR_TEXT

    def test_result_is_tuple(self):
        res = square_equation_solver(0, 0, 0)
        assert isinstance(res, tuple)

    # Параметризация лучше цикла тем, что когда в цикле упадет исключение,
    # то цикл дальше продолжаться не будет.
    # А при параметризации выполнятся все тесты.

    @pytest.mark.parametrize(
        'args, expected_result',
        [
            ((1, -3, -4), (4, -1)),
            ((0, 0, 1), (None, None)),
            pytest.param((1, -3, -4), (4, -1), id='general'),
            pytest.param((0, 0, 1), (None, None), id='no results'),
        ]
    )
    def test_solves_ok(self, args, expected_result):
        res = square_equation_solver(*args)
        assert res == expected_result

# вызов фикстуры внутри parametrize

@pytest.fixture
def x(request):
    return request.param * 3


@pytest.fixture
def y(request):
    return request.param * 2

@pytest.mark.parametrize(
    "x, y",
    [
        ('a', 'b'),
    ],
    indirect=['x']
)
def test_indirect(x, y):
    assert x == 'aaa'
    assert y == 'b'

