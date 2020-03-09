import random
from game.game import (
    TwentyFortyEight,
)
from game.mechanics import (
    DOWN, RIGHT,
)


def test_new():
    random.seed(1234)
    state = TwentyFortyEight.new()
    expected_state = {
        'board': [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]],
        'score': 0,
        'gameover': False,
    }
    assert state == expected_state


def test_state():
    random.seed(1234)
    state = TwentyFortyEight().state
    expected_state = {
        'board': [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]],
        'score': 0,
        'gameover': False,
    }
    assert state == expected_state


def test_update():
    random.seed(1234)
    expected_state = {
        'board': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 4, 2, 0]],
        'score': 0,
        'gameover': False,
    }
    state = {
        'board': [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]],
        'score': 0,
        'gameover': False,
    }
    down = 2
    state = TwentyFortyEight.update(state, direction=down)
    assert state == expected_state


def test_blank_board_rows_cols():
    expected_num_position = 2
    game = TwentyFortyEight(rows=2, cols=2)
    available_positions = game._get_available_positions()
    assert available_positions is not None
    assert len(available_positions) == expected_num_position


def test_board():
    expected_state = {
        'board': [
            [2, 8],
            [4, 0]
        ],
        'score': 0,
        'gameover': False,
    }
    state = {
        'board': [
            [2, 8],
            [4, 0]
        ],
        'score': 0,
        'gameover': False,
    }
    game = TwentyFortyEight._load(state)
    assert game.state == expected_state


def test_move_down():
    random.seed(1234)
    expected_state = {
        'board': [
            [2, 0],
            [4, 16],
        ],
        'score': 16,
        'gameover': False,
    }
    state = {
        'board': [
            [0, 8],
            [4, 8],
        ],
        'score': 0,
        'gameover': False,
    }
    game = TwentyFortyEight._load(state)._move(DOWN)
    assert game.state == expected_state


def test_gameover():
    state = {
        'board': [
            [2, 8],
            [4, 0],
        ],
        'score': 0,
        'gameover': False,
    }
    game = TwentyFortyEight._load(state)._move(DOWN)
    assert game.gameover


def test_double_move():
    expected_first_score = 8 + 8
    expected_second_score = expected_first_score + 16 + 16
    state = {
        'board': [
            [0, 8],
            [16, 8],
        ],
        'score': 0,
        'gameover': False,
    }
    game = TwentyFortyEight._load(state)
    game._move(DOWN)
    assert game.score == expected_first_score
    game._move(RIGHT)
    assert game.score == expected_second_score
