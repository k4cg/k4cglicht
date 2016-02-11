"""Alarm mode
 Make the bulbs blink in red and white
in a very short time
"""
import time
from mode import Mode
class Alarm(Mode):


    @staticmethod
    def get_params():
        return ('alarm', None)

    @staticmethod
    def execute(light_utils, args=None):
        for x in range(1, 7):
            light_utils.set_light("Red")
            time.sleep(1)
            light_utils.set_light("Moccasin")
            time.sleep(0.5)
