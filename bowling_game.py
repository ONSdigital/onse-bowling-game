TOTAL_FRAMES = 10


class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(TOTAL_FRAMES):
            if self._frame_score(roll_index) == 10:
                total_score += 10 + self.rolls[roll_index + 2]
            else:
                total_score += self._frame_score(roll_index)
            roll_index += 2

        return total_score

    def _frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
