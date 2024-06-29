from functools import reduce


class Game:
    def __init__(self, rolls=None, current_roll=0) -> None:
        self.rolls = rolls if rolls is not None else [0] * 21
        self.current_roll = current_roll

    def roll(self, pins):
        def add_pins_to_rolls():
            return (self.rolls[:self.current_roll] +
                    [pins] + self.rolls[self.current_roll+1:])

        return Game(add_pins_to_rolls(), self.current_roll + 1)

    @ property
    def score(self):
        def is_strike(frame_index):
            return self.rolls[frame_index] == 10

        def is_spare(frame_index):
            return self.rolls[frame_index] + self.rolls[frame_index+1] == 10

        def strike_bonus(frame_index):
            return self.rolls[frame_index+1] + self.rolls[frame_index+2]

        def spare_bonus(frame_index):
            return self.rolls[frame_index+2]

        def frame_score(frame_index):
            return self.rolls[frame_index] + self.rolls[frame_index+1]

        def score_per_frame(acc, _):
            score, frame_index = acc

            if is_strike(frame_index):
                return (score + 10 + strike_bonus(frame_index), frame_index + 1)
            if is_spare(frame_index):
                return (score + 10 + spare_bonus(frame_index), frame_index + 2)
            return (score + frame_score(frame_index), frame_index + 2)

        def total_score():
            score, _ = reduce(score_per_frame, range(10), (0, 0))
            return score

        return total_score()
