# Clone of 2048 game for Principles of Computing Coursera class
# @jbutewicz
# Adapted by Joseph Stockermans


import random
from game.exceptions import (
    GameOver,
)
from game.mechanics import (
    move,
)


class TwentyFortyEight:
    """
    Logic for a 2048 style game.
    """

    def __init__(self, rows=None, cols=None, board=None, score=0):
        """
        Not to be called directly. Game initialization should occur through
        `game.TwentyFortyEight.new or `game.TwentyFortyEight.load`.

        :param rows: the number of rows on the board grid. Must be provided
            along with `cols`.
        :type rows: `int`
        :param cols: the number of columns on the board. Must be provided
            along with `rows`.
        :type cols: `int`
        :param board: the list of lists representing the board. No need to
            specifiy `rows` or cols`.
        :type board: `list`
        :param score: the player's score.
        :type score: `int`
        """
        self.board = board or TwentyFortyEight._blank(rows, cols)
        self.rows = rows or len(self.board)
        self.cols = cols or len(self.board[0])
        self.score = score

    @staticmethod
    def _blank(rows, cols):
        """
        Return a blank board.

        :param rows: the number of rows on the board grid.
        :type rows: `int`
        :param cols: the number of columns on the board.
        :type cols: `int`
        :returns: `list` -- the list of lists representing the board.
        """
        return [[0 for j in range(cols)] for i in range(rows)]

    @classmethod
    def new(cls, rows, cols):
        """
        Initialize a new game.

        :param rows: the number of rows on the board grid.
        :type rows: `int`
        :param cols: the number of columns on the board.
        :type cols: `int`
        :returns: instance of `game.TwentyFortyEight` -- the game object
        """
        game = cls(rows, cols)
        game._new_tile()
        game._new_tile()
        return game

    @classmethod
    def load(cls, board, score):
        """
        Initialize a game from a given board and score.

        :param board: the list of lists representing the board.
        :type board: `list`
        :param score: the player's score.
        :type score: `int`
        :returns: instance of `game.TwentyFortyEight` -- the game object
        """
        game = cls(board=board, score=score)
        return game

    def move(self, direction):
        """
        Perform a move.

        :param direction: the direction to move the board tiles. UP = 1,
            DOWN = 2, LEFT = 3, RIGHT = 4
        :type direction: `integer`
        :returns: board and score
        """
        board, score_increment = move(self.board, direction)
        self.board = board
        self.score += score_increment
        self._new_tile()
        return self.board, self.score

    def _new_tile(self):
        # Create a new tile in a randomly selected empty
        # square.  The tile should be 2 90% of the time and
        # 4 10% of the time.
        available_positions = self._get_available_positions()
        if len(available_positions) == 1:
            raise GameOver
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
