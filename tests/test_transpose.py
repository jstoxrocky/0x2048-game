from game.fundamentals import (
    transpose,
)


def test_2x2():
    expected_output = [
        [2, 4],
        [8, 0]
    ]
    _input = [
        [2, 8],
        [4, 0]
    ]
    output = transpose(_input)
    assert output == expected_output


def test_3x3():
    expected_output = [
        [2, 4, 0],
        [8, 4, 2],
        [8, 0, 0],
    ]
    _input = [
        [2, 8, 8],
        [4, 4, 0],
        [0, 2, 0],
    ]
    output = transpose(_input)
    assert output == expected_output
