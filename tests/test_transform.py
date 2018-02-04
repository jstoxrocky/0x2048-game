from game.mechanics import (
    transform,
    UP, DOWN, LEFT, RIGHT
)


def test_2x2_up():
    expected_output = [
        [4, 2],
        [8, 0]
    ]
    _input = [
        [2, 0],
        [4, 8]
    ]
    output = transform(_input, UP)
    assert output == expected_output


def test_2x2_down():
    expected_output = [
        [8, 0],
        [2, 4]
    ]
    _input = [
        [2, 8],
        [4, 0]
    ]
    output = transform(_input, DOWN)
    assert output == expected_output


def test_2x2_left():
    expected_output = [
        [8, 2],
        [4, 0]
    ]
    _input = [
        [2, 8],
        [0, 4]
    ]
    output = transform(_input, LEFT)
    assert output == expected_output


def test_2x2_right():
    expected_output = [
        [8, 2],
        [4, 0]
    ]
    _input = [
        [8, 2],
        [4, 0]
    ]
    output = transform(_input, RIGHT)
    assert output == expected_output


def test_2x2_down_with_a_resulting_zero_row():
    expected_output = [
        [8, 0],
        [0, 4]
    ]
    _input = [
        [0, 8],
        [4, 0]
    ]
    output = transform(_input, DOWN)
    assert output == expected_output
