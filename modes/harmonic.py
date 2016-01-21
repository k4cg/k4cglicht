from mode import Mode
from default import Default
import random
import time

class Harmonic(Mode):

    @staticmethod
    def name():
        return ['harmonisch ausrasten', 'harmonisch']

    @staticmethod
    def execute(light_utils, args=None):
        length = 50 if not args else int(args.values()[0])
        for x in range(1, length):
            brightness = random.randrange(1,100)
            color = random.choice(light_utils.colors.keys())
            light_utils.set_light(color, transition = 10, brightness = brightness)
            time.sleep(1.3)
        Default.execute(light_utils)
