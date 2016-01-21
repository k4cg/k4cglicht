from mode import Mode

class Default(Mode):

    @staticmethod
    def name():
        return 'normal'

    @staticmethod
    def execute(light_utils, args=None):
        light_utils.set_light(colorname="Moccasin", brightness=59)
