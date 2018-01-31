import pytest
from game.game import (
    TwentyFortyEight,
)
from game.mechanics import (
    DOWN, RIGHT,
)
from game.exceptions import (
    GameOver,
)


def test_blank_board_rows_cols():
    expected_num_position = 2
    game = TwentyFortyEight.new(2, 2)
    available_positions = game._get_available_positions()
    assert available_positions is not None
    assert len(available_positions) == expected_num_position


def test_board():
    expected_board = [
        [2, 8],
        [4, 0]
    ]
    expected_score = 0
    board_input = [
        [2, 8],
        [4, 0]
    ]
    game = TwentyFortyEight.load(board=board_input, score=expected_score)
    assert game.board == expected_board
    assert game.score == expected_score


def test_move_down():
    expected_bottom_row = [4, 16]
    expected_score = 16
    _input = [
        [0, 8],
        [4, 8]
    ]
    game = TwentyFortyEight.load(board=_input, score=0)
    board, score = game.move(DOWN)
    _, bottom_row = board
    assert expected_bottom_row == bottom_row
    assert score == expected_score


def test_gameover():
    _input = [
        [2, 8],
        [4, 0]
    ]
    game = TwentyFortyEight.load(board=_input, score=0)
    with pytest.raises(GameOver):
        game.move(DOWN)


def test_double_move():
    expected_first_score = 8 + 8
    expected_second_score = expected_first_score + 16 + 16
    _input = [
        [0, 8],
        [16, 8]
    ]
    game = TwentyFortyEight.load(board=_input, score=0)
    board, score = game.move(DOWN)
    assert score == expected_first_score
    board, score = game.move(RIGHT)
    assert score == expected_second_score
