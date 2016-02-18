from mode import Mode

class Color(Mode):

    @staticmethod
    def get_params():
        return ('farbe', 'colorname')

    @staticmethod
    def execute(light_utils, argument=None):
        light_utils.set_light(argument)
