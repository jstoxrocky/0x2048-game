from game.mechanics import (
    filter_out_zeros,
)


def test_0_0_0():
    expected_output = []
    _input = [0, 0, 0]
    output = filter_out_zeros(_input)
    assert output == expected_output


def test_0_1_0():
    expected_output = [1]
    _input = [0, 1, 0]
    output = filter_out_zeros(_input)
    assert output == expected_output


def test_1_0_0():
    expected_output = [1]
    _input = [1, 0, 0]
    output = filter_out_zeros(_input)
    assert output == expected_output


def test_0_0_1():
    expected_output = [1]
    _input = [0, 0, 1]
    output = filter_out_zeros(_input)
    assert output == expected_output


def test_1_2_3():
    expected_output = [1, 2, 3]
    _input = [1, 2, 3]
    output = filter_out_zeros(_input)
    assert output == expected_output
