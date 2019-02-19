from bowling_game import BowlingGame


def test_gutter_game():
    game = BowlingGame()

    roll_many(game, count=20, pins=0)

    assert game.score() == 0


def test_all_ones():
    game = BowlingGame()

    roll_many(game, count=20, pins=1)

    assert game.score() == 20


def roll_many(game, count, pins):
    for roll in range(count):
        game.roll(pins)
