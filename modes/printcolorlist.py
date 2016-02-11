from mode import Mode

class PrintColorList(Mode):

    @staticmethod
    def get_params():
        return ('farben', None)

    @staticmethod
    def execute(light_utils, argument=None):
        light_utils.print_all_colors()
