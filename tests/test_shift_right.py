from game.fundamentals import (
    shift_right,
)


def test_2x2_no_match():
    expected_board = [
        [2, 8],
        [0, 4]
    ]
    expected_score = 0
    _input = [
        [2, 8],
        [4, 0]
    ]
    board, score = shift_right(_input)
    assert board == expected_board
    assert score == expected_score


def test_2x2_match():
    expected_board = [
        [2, 8],
        [0, 8]
    ]
    expected_score = 8
    _input = [
        [2, 8],
        [4, 4]
    ]
    board, score = shift_right(_input)
    assert board == expected_board
    assert score == expected_score


def test_3x3_no_match():
    expected_board = [
        [2, 8, 4],
        [0, 0, 4],
        [0, 0, 2],
    ]
    expected_score = 0
    _input = [
        [2, 8, 4],
        [4, 0, 0],
        [0, 2, 0],
    ]
    board, score = shift_right(_input)
    assert board == expected_board
    assert score == expected_score


def test_3x3_match():
    expected_board = [
        [0, 2, 16],
        [0, 0, 8],
        [0, 0, 2],
    ]
    expected_score = 8 + 16
    _input = [
        [2, 8, 8],
        [4, 4, 0],
        [0, 2, 0],
    ]
    board, score = shift_right(_input)
    assert board == expected_board
    assert score == expected_score
