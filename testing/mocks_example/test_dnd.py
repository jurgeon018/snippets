from unittest import mock
from dnd import attack_damage1, attack_damage2

'''
Few common gotchas that can trip you up when mocking.
When specifying the path to what you wanna patch you need to take care
to point to where its being used, but not where its defined.

autospec=True makes sure that anything mock
tries to mimic it's original a bit more closely.

Mock with autospec=False will take anythink you throw at it.
Which isn't too useful when you are testing.
Mock with autospec=True our mocked function will check the right
number of arguments.
'''


@mock.patch('dnd.randint', return_value=5, autospec=True)
def test_attack_damage1(mock_randint):
    # this will pass
    assert attack_damage1(1) == 6
    mock_randint.assert_called_one_with(1, 8)


@mock.patch('dnd.randint', return_value=5)
def test_attack_damage2(mock_randint):
    # this will pass
    assert attack_damage1(1) == 6
    mock_randint.assert_called_one_with(1, 8)


@mock.patch('dnd.randint', return_value=5, autospec=True)
def test_attack_damage1(mock_randint):
    # this will fail
    # assert attack_damage2(1) == 6
    pass


@mock.patch('dnd.randint', return_value=5)
def test_attack_damage2(mock_randint):
    # this will pass
    assert attack_damage2(1) == 6
    # mock_randint.assert_called_one_with(1, 8)


@mock.patch('random.randint', return_value=5, autospec=True)
def test_attack_damage3(mock_randint):
    # this will fail
    # assert attack_damage1(1) == 6
    pass
