from functools import reduce
from bowling_game import Game


def roll_many(pins, n):
    return [pins] * n


def roll_spare():
    return [5, 5, 3]


def roll_strike():
    return [10, 3, 4]


def play_rolls(rolls):
    def play(game, roll):
        return game.roll(roll)

    return reduce(play, rolls, Game())


def test_gutter_game():
    game = play_rolls(roll_many(0, 20))
    assert game.score == 0


def test_all_ones():
    game = play_rolls(roll_many(1, 20))
    assert game.score == 20


def test_one_spare():
    game = play_rolls(roll_spare() + roll_many(0, 17))
    assert game.score == 16


def test_one_strike():
    game = play_rolls(roll_strike() + roll_many(0, 16))
    assert game.score == 24


def test_perfect_game():
    game = play_rolls(roll_many(10, 12))
    assert game.score == 300
