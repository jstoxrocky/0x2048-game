from game.fundamentals import (
    transform_back,
    UP, DOWN, LEFT, RIGHT
)


def test_2x2_up():
    _input = [
        [4, 2],
        [8, 0]
    ]
    expected_output = [
        [2, 0],
        [4, 8]
    ]
    output = transform_back(_input, UP)
    assert output == expected_output


def test_2x2_down():
    _input = [
        [8, 0],
        [2, 4]
    ]
    expected_output = [
        [2, 8],
        [4, 0]
    ]
    output = transform_back(_input, DOWN)
    assert output == expected_output


def test_2x2_left():
    _input = [
        [8, 2],
        [4, 0]
    ]
    expected_output = [
        [2, 8],
        [0, 4]
    ]
    output = transform_back(_input, LEFT)
    assert output == expected_output


def test_2x2_right():
    _input = [
        [8, 2],
        [4, 0]
    ]
    expected_output = [
        [8, 2],
        [4, 0]
    ]
    output = transform_back(_input, RIGHT)
    assert output == expected_output


def test_2x2_down_with_a_resulting_zero_row():
    _input = [
        [8, 0],
        [0, 4]
    ]
    expected_output = [
        [0, 8],
        [4, 0]
    ]
    output = transform_back(_input, DOWN)
    assert output == expected_output
