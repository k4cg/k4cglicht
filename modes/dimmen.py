from mode import Mode

class Dimmen(Mode):

    @staticmethod
    def name():
        return 'dimmen'

    @staticmethod
    def execute(light_utils, args=None):
        light_utils.dim_light(args.values()[0])
