from mode import Mode
from default import Default
import random
import time

class RandomColors(Mode):

    @staticmethod
    def get_params():
        return [('zufall', None), ('alieninvasion', 'duration')]

    @staticmethod
    def execute(light_utils, argument=None):
        length = 50 if not argument or argument is True else int(argument)
        for x in range(0, length):
            color = random.choice(light_utils.colors.keys())
            light_utils.set_light(color)
            time.sleep(0.5)
        Default.execute(light_utils)
