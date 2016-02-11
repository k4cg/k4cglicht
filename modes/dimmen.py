from mode import Mode

class Dimmen(Mode):

    @staticmethod
    def get_params():
        return ('dimmen', 'percentage')

    @staticmethod
    def execute(light_utils, argument=None):
        light_utils.dim_light(argument)
