from bowling_game import BowlingGame


def test_gutter_game():
    game = BowlingGame()

    for roll in range(20):
        game.roll(0)

    assert game.score() == 0


def test_all_ones():
    game = BowlingGame()

    for roll in range(20):
        game.roll(1)

    assert game.score() == 20
