UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


def transpose(matrix):
    """
    Performs a matrix transpose
    """
    transposition = [list(row) for row in zip(*matrix)]
    return transposition


def filter_out_zeros(row):
    """
    Removes all zeros from a row
    """
    filtered = list(filter(lambda x: x != 0, row))
    return filtered


def pad_left(row, length):
    """
    Pads zeros to the left of a row to match a given length
    """
    difference = length - len(row)
    padded = [0] * difference + row
    return padded


def condense(arr, result=None, score=0):
    """
    Condenses a row of numbers by doubling matching adjascent values
    according to the rules of 2048
    """
    result = result or []
    # If the list is a single value
    # There can be no matches, so record the value
    if len(arr) == 1:
        result.append(arr[0])
    # Iterate over the list
    for i in range(1, len(arr)):
        # If two values in a row are equal
        # Multiply the first value by two
        # Record it
        # Chop off those two values from out input list
        # Repeat
        if arr[i] == arr[i - 1]:
            m = 2
            inc = 1
            score += arr[i - 1] * m
        # Otherwise,
        # Multiply the first value by one
        # Record it
        # Chop off that one value from the input list
        # Repeat
        else:
            m = 1
            inc = 0
        # Multiply result by our multiplier `m`
        value = arr[i - 1] * m
        # Record
        result.append(value)
        # Chop off our list according to our list index incrementer `inc`
        new_arr = arr[i + inc:]
        # Repeat
        result, score = condense(new_arr, result, score)
        break
    return result, score


def shift_right(board):
    """
    Shifts the blocks to the right
    """
    size = len(board[0])
    filtered = [filter_out_zeros(row) for row in board]
    # Reverse so that we condense values closest to edge first
    reverse = [row[::-1] for row in filtered]
    # Condense the rows and get the score
    score = 0
    condensed = []
    for row in reverse:
        condensed_row, score_increment = condense(row)
        condensed.append(condensed_row)
        score += score_increment
    # Reverse back
    reverse = [row[::-1] for row in condensed]
    padded = [pad_left(row, size) for row in reverse]
    return padded, score


def transform(board, direction):
    """
    Transforms the board so that a rightward shift
    will be equivalent to whatever direction we want to shift the blocks
    """
    if direction in {UP}:
        board = transpose(board)
        board = [row[::-1] for row in board]
    if direction in {DOWN}:
        board = [row[::-1] for row in board]
        board = transpose(board)
    if direction in {LEFT}:
        board = [row[::-1] for row in board]
    return board


def transform_back(board, direction):
    """
    Reverses the transformation performed by the `transform` function,
    getting out original board setup back
    """
    if direction in {UP}:
        board = [row[::-1] for row in board]
        board = transpose(board)
    if direction in {DOWN}:
        board = transpose(board)
        board = [row[::-1] for row in board]
    if direction in {LEFT}:
        board = [row[::-1] for row in board]
    return board


def move(board, direction):
    """
    Moves the blocks in the direction specified
    """
    board = transform(board, direction)
    board, score = shift_right(board)
    board = transform_back(board, direction)
    return board, score
