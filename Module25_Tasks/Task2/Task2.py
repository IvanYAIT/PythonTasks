import random as rnd
import os

class KarmaCollector:
    MAX_KARMA = 500
    PATH_TO_KARMA_LOG = os.path.abspath(__file__).replace('Task1.py', 'karma.log')
    current_karma = 0

    def try_your_luck(self):
        number = rnd.randint(1, 10)
        ERRORS = [KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]
        try:
            if number == 1:
                raise ERRORS[rnd.randint(0, len(ERRORS)-1)]
        except Exception as e:
            with open(self.PATH_TO_KARMA_LOG, '+a') as file:
                file.write(f'{e.__class__.__name__}\n')

    def one_day(self):
        self.current_karma += rnd.randint(1, 7)
        self.try_your_luck()

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass