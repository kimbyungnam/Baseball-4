import pytest

from game import Game
from game_result import GameResult


@pytest.fixture()
def game():
    return Game()


def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)


def assert_matched_number(result: GameResult, *, solved: bool, strikes: int, balls: int):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls


@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "12s", "121"])
def test_exception_when_input_invalid_input(game, invalid_input):
    assert_illegal_argument(game, invalid_input)


def test_return_solved_result_if_matched_number(game):
    game.question = "123"

    result: GameResult = game.guess("123")

    assert_matched_number(result, solved=True, strikes=3, balls=0)


def test_return_solved_result_if_unmatched_number(game):
    game.question = "123"

    result: GameResult = game.guess("456")

    assert_matched_number(result, solved=False, strikes=0, balls=0)


@pytest.mark.parametrize("input", ["124", "143"])
def test_return_solved_result_if_2_strikes_0_ball_number(game, input):
    game.question = "123"

    result: GameResult = game.guess(input)

    assert_matched_number(result, solved=False, strikes=2, balls=0)


def test_return_solved_result_if_1_strikes_2_ball_number(game):
    game.question = "123"

    result: GameResult = game.guess("132")

    assert_matched_number(result, solved=False, strikes=1, balls=2)