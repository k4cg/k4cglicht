from mode import Mode

class Default(Mode):

    @staticmethod
    def get_params():
        return ('normal', None)

    @staticmethod
    def execute(light_utils, argument=None):
        light_utils.set_light("Moccasin", brightness=59, transition=10)
