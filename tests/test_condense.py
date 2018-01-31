from game.fundamentals import (
    condense,
)


def test_no_matches():
    expected_output = [2, 4, 8]
    expected_score = 0
    _input = [2, 4, 8]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score


def test_only_two_matches():
    expected_output = [4, 16]
    expected_score = 4 + 16
    _input = [2, 2, 8, 8]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score


def test_one_match_and_one_on_end():
    expected_output = [4, 8]
    expected_score = 4
    _input = [2, 2, 8]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score


def test_two_matches_and_one_on_end():
    expected_output = [4, 16, 4]
    expected_score = 4 + 16
    _input = [2, 2, 8, 8, 4]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score


def test_one_match_and_matching_initial_value_on_end():
    expected_output = [4, 2]
    expected_score = 4
    _input = [2, 2, 2]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score


def test_one_match_and_matching_doubled_value_on_end():
    expected_output = [4, 4]
    expected_score = 4
    _input = [2, 2, 4]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score


def test_two_matches_and_matching_doubled_value_on_end():
    expected_output = [4, 16, 16]
    expected_score = 4 + 16
    _input = [2, 2, 8, 8, 16]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score


def test_non_match_at_start_followed_by_match():
    expected_output = [2, 16, 16]
    expected_score = 16
    _input = [2, 8, 8, 16]
    output, score = condense(_input)
    assert output == expected_output
    assert score == expected_score
