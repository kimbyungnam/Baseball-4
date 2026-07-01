from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number: str) -> GameResult | None:
        self._assert_illegal_value(guess_number)

        if guess_number == self._question:
            return GameResult(True, 3, 0)

        strikes = sum(
            1
            for number, question in zip(guess_number, self._question)
            if number == question
        )

        balls = 0
        if guess_number[0] in self._question:
            balls += 1
        if guess_number[1] in self._question:
            balls += 1
        if guess_number[2] in self._question:
            balls += 1
        balls -= strikes

        return GameResult(False, strikes, balls)

    def _assert_illegal_value(self, guess_number: str):
        if guess_number is None:
            raise TypeError()

        if len(guess_number) != 3:
            raise TypeError()

        if not guess_number.isdigit():
            raise TypeError()

        if self._is_duplicate_number(guess_number):
            raise TypeError()

    def _is_duplicate_number(self, guess_number: str) -> bool:
        return len(set(guess_number)) != 3
