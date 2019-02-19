import pytest

from bowling_game import BowlingGame


@pytest.fixture
def game():
    return BowlingGame()


def test_gutter_game(game):
    roll_many(game, count=20, pins=0)

    assert game.score() == 0


def test_all_ones(game):
    roll_many(game, count=20, pins=1)

    assert game.score() == 20


# def test_spare(game):
#     game.roll(5)
#     game.roll(5)  # spare
#     game.roll(1)
#
#     assert game.score() == 12


def roll_many(game, count, pins):
    for roll in range(count):
        game.roll(pins)
