from game.mechanics import (
    pad_left,
)


def test_0_0():
    expected_output = [0, 0, 0, 0]
    _input = [0, 0]
    output = pad_left(_input, 4)
    assert output == expected_output


def test_0_0_1():
    expected_output = [0, 0, 0, 1]
    _input = [0, 0, 1]
    output = pad_left(_input, 4)
    assert output == expected_output


def test_1_2_3():
    expected_output = [0, 1, 2, 3]
    _input = [1, 2, 3]
    output = pad_left(_input, 4)
    assert output == expected_output


def test_0_1_2():
    expected_output = [0, 0, 1, 2]
    _input = [0, 1, 2]
    output = pad_left(_input, 4)
    assert output == expected_output
