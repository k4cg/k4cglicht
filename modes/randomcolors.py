from mode import Mode
from default import Default
import random
import time

class RandomColors(Mode):

    @staticmethod
    def name():
        return ['zufall', 'alieninvasion']

    @staticmethod
    def execute(light_utils, args=None):
        length = 50 if not args else int(args.values()[0])
        for x in range(0, length):
            color = random.choice(light_utils.colors.keys())
            light_utils.set_light(color, brightness = 100, transition = 1)
            time.sleep(0.7)
        Default.execute(light_utils)
