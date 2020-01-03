# Clone of 2048 game for Principles of Computing Coursera class
# @jbutewicz
# Adapted by Joseph Stockermans


import random
from game import (
    mechanics,
)


class TwentyFortyEight:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.gameover = False
        self.score = 0
        self.board = TwentyFortyEight._empty_board(self.rows, self.cols)
        self._add_new_tile()
        self._add_new_tile()

    @staticmethod
    def _empty_board(rows, cols):
        return [[0 for j in range(cols)] for i in range(rows)]

    @classmethod
    def _load(cls, state):
        rows = len(state['board'])
        cols = len(state['board'][0])
        game = TwentyFortyEight(rows=rows, cols=cols)
        game.board = state['board']
        game.score = state['score']
        game.gameover = state['gameover']
        return game

    @classmethod
    def update(cls, state, direction):
        game = TwentyFortyEight._load(state)._move(direction)
        return game.state

    @property
    def state(self):
        return {
            'board': self.board,
            'score': self.score,
            'gameover': self.gameover,
        }

    def _move(self, direction):
        board, score_increment = mechanics.move(self.board, direction)
        self.board = board
        self.score += score_increment
        self._add_new_tile()
        return self

    def _add_new_tile(self):
        # Create a new tile in a randomly selected empty
        # square.  The tile should be 2 90% of the time and
        # 4 10% of the time.
        available_positions = self._get_available_positions()
        if len(available_positions) == 1:
            self.gameover = True
        else:
            random_tile = random.choice(available_positions)
            weighted_choices = [(2, 9), (4, 1)]
            population = [
                val for val, cnt in weighted_choices for i in range(cnt)
            ]
            tile = random.choice(population)
            row, col = random_tile
            self._set_tile(row, col, tile)

    def _get_available_positions(self):
        available_positions = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    available_positions.append([row, col])
        return available_positions

    def _set_tile(self, row, col, value):
        self.board[row][col] = value
