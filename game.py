class Game:
    def guess(self, guess_number):
        if guess_number is None:
            raise TypeError()