class Game:
    def guess(self, guess_number: str):
        self._assert_illegal_value(guess_number)

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
