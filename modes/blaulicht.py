import time
from mode import Mode
from default import Default

class Blaulicht(Mode):

    @staticmethod
    def name():
        return 'blaulicht'

    @staticmethod
    def execute(light_utils, args=None):
        for x in range(0, 7):
            light_utils.set_light("Blue")
            time.sleep(0.7)
            light_utils.set_light("Moccasin")
            time.sleep(0.7)
            light_utils.set_light("Red")
            time.sleep(0.5)
        Default.execute(light_utils)
