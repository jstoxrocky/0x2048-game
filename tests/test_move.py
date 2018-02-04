from game.mechanics import (
    move,
    UP, DOWN, LEFT, RIGHT
)


def test_2x2_up():
    expected_board = [
        [2, 8],
        [4, 0]
    ]
    expected_score = 0
    _input = [
        [2, 0],
        [4, 8]
    ]
    board, score = move(_input, UP)
    assert board == expected_board
    assert score == expected_score


def test_2x2_down():
    expected_board = [
        [2, 0],
        [4, 8]
    ]
    expected_score = 0
    _input = [
        [2, 8],
        [4, 0]
    ]
    board, score = move(_input, DOWN)
    assert board == expected_board
    assert score == expected_score


def test_2x2_left():
    expected_board = [
        [2, 8],
        [4, 0]
    ]
    expected_score = 0
    _input = [
        [2, 8],
        [0, 4]
    ]
    board, score = move(_input, LEFT)
    assert board == expected_board
    assert score == expected_score


def test_2x2_right():
    expected_board = [
        [8, 2],
        [0, 4]
    ]
    expected_score = 0
    _input = [
        [8, 2],
        [4, 0]
    ]
    board, score = move(_input, RIGHT)
    assert board == expected_board
    assert score == expected_score


def test_2x2_up_match():
    expected_board = [
        [2, 16],
        [4, 0]
    ]
    expected_score = 16
    _input = [
        [2, 8],
        [4, 8]
    ]
    board, score = move(_input, UP)
    assert board == expected_board
    assert score == expected_score


def test_3x3_up_match():
    expected_board = [
        [4, 16, 8],
        [0, 2, 4],
        [0, 0, 0],
    ]
    expected_score = 4 + 16 + 8
    _input = [
        [2, 8, 4],
        [0, 8, 4],
        [2, 2, 4],
    ]
    board, score = move(_input, UP)
    assert board == expected_board
    assert score == expected_score
