from BridgeWrapper import BridgeWrapper
import time
import sys

class LightUtils(object):

    def __init__(self, config):

        self.bridge_wrapper = BridgeWrapper(config)
        self.colors = \
            {
                'Blue': [0.139, 0.081],
                'Pink': [0.3944, 0.3093],
                'Honeydew': [0.316, 0.3477],
                'Spring Green': [0.1994, 0.5864],
                'Purple': [0.2651, 0.1291],
                'Fuchsia': [0.3787, 0.1724],
                'Dark Salmon': [0.4837, 0.3479],
                'Dodger Blue': [0.1484, 0.1599],
                'Crimson': [0.6531, 0.2834],
                'White': [0.3227, 0.329],
                'Lime Green': [0.2101, 0.6765],
                'Cornsilk': [0.3511, 0.3574],
                'Bisque': [0.3806, 0.3576],
                'Brown': [0.6399, 0.3041],
                'Medium Aquamarine': [0.215, 0.4014],
                'Chocolate': [0.6009, 0.3684],
                'Dark Goldenrod': [0.5265, 0.4428],
                'Dark Blue': [0.139, 0.081],
                'Dark Slate Blue': [0.2206, 0.1484],
                'Light Cyan': [0.2901, 0.3316],
                'Lavender Blush': [0.3369, 0.3225],
                'Light Green': [0.2648, 0.4901],
                'Olive': [0.4432, 0.5154],
                'Slate Blue': [0.2218, 0.1444],
                'Lawn Green': [0.2663, 0.6649],
                'Old Lace': [0.3421, 0.344],
                'Plum': [0.3495, 0.2545],
                'Medium Orchid': [0.3365, 0.1735],
                'Medium Purple': [0.263, 0.1773],
                'Royal Blue': [0.1649, 0.1338],
                'Rebecca Purple': [0.2703, 0.1398],
                'Dark Sea Green': [0.2924, 0.4134],
                'Light Goldenrod': [0.3504, 0.3717],
                'Orange Red': [0.6726, 0.3217],
                'Midnight Blue': [0.1585, 0.0884],
                'White Smoke': [0.3227, 0.329],
                'Alice Blue': [0.3088, 0.3212],
                'Medium Violet Red': [0.504, 0.2201],
                'Tan': [0.4035, 0.3772],
                'Dark Orchid': [0.296, 0.1409],
                'Dark Cyan': [0.17, 0.3403],
                'Magenta': [0.3787, 0.1724],
                'Medium Spring Green': [0.1919, 0.524],
                'Web Gray': [0.3227, 0.329],
                'Sea Green': [0.1968, 0.5047],
                'Chartreuse': [0.2682, 0.6632],
                'Navajo White': [0.4027, 0.3757],
                'Per': [0.5305, 0.3911],
                'Orange': [0.5614, 0.4156],
                'Red': [0.7, 0.2986],
                'Cornflower': [0.1905, 0.1945],
                'Light Salmon': [0.5016, 0.3531],
                'Wheat': [0.3852, 0.3737],
                'Dark Turquoise': [0.1693, 0.3347],
                'Floral White': [0.3361, 0.3388],
                'Cyan': [0.17, 0.3403],
                'Turquoise': [0.1732, 0.3672],
                'Gainsboro': [0.3227, 0.329],
                'Gray': [0.3227, 0.329],
                'Thistle': [0.3342, 0.2971],
                'Moccasin': [0.3927, 0.3732],
                'Navy Blue': [0.139, 0.081],
                'Steel Blue': [0.183, 0.2325],
                'Forest Green': [0.2097, 0.6732],
                'Light Sky Blue': [0.214, 0.2749],
                'Green': [0.214, 0.709],
                'Beige': [0.3402, 0.356],
                'Teal': [0.17, 0.3403],
                'Azure': [0.3059, 0.3303],
                'Sky Blue': [0.2206, 0.2948],
                'Medium Sea Green': [0.1979, 0.5005],
                'Blue Violet': [0.245, 0.1214],
                'Mint Cream': [0.315, 0.3363],
                'Hot Pink': [0.4682, 0.2452],
                'Lavender': [0.3085, 0.3071],
                'Light Sea Green': [0.1721, 0.358],
                'Violet': [0.3644, 0.2133],
                'Dark Green': [0.214, 0.709],
                'Peach Puff': [0.3953, 0.3564],
                'Cadet Blue': [0.2211, 0.3328],
                'Ghost White': [0.3174, 0.3207],
                'Burlywood': [0.4236, 0.3811],
                'Web Maroon': [0.7, 0.2986],
                'Snow': [0.3292, 0.3285],
                'Light Coral': [0.5075, 0.3145],
                'Light Steel Blue': [0.276, 0.2975],
                'Black': [0.139, 0.081],
                'Medium Turquoise': [0.176, 0.3496],
                'Sandy Brown': [0.5104, 0.3826],
                'Ivory': [0.3334, 0.3455],
                'Salmon': [0.5346, 0.3247],
                'Web Green': [0.214, 0.709],
                'Light Slate Gray': [0.2738, 0.297],
                'Pale Green': [0.2675, 0.4826],
                'Yellow': [0.4432, 0.5154],
                'Tomato': [0.6112, 0.3261],
                'Dim Gray': [0.3227, 0.329],
                'Dark Magenta': [0.3787, 0.1724],
                'Aqua': [0.17, 0.3403],
                'Slate Gray': [0.2762, 0.3009],
                'Light Blue': [0.2621, 0.3157],
                'Green Yellow': [0.3298, 0.5959],
                'Lemon Chiffon': [0.3608, 0.3756],
                'Indigo': [0.2332, 0.1169],
                'Gold': [0.4947, 0.472],
                'Rosy Brown': [0.4026, 0.3227],
                'Pale Turquoise': [0.2539, 0.3344],
                'Dark Violet': [0.2742, 0.1326],
                'Sienna': [0.5714, 0.3559],
                'Misty Rose': [0.3581, 0.3284],
                'Indian Red': [0.5488, 0.3112],
                'Dark Slate Gray': [0.2239, 0.3368],
                'Dark Olive Green': [0.3475, 0.5047],
                'Light Pink': [0.4112, 0.3091],
                'Lime': [0.214, 0.709],
                'Dark Orange': [0.5951, 0.3872],
                'Yellow Green': [0.3517, 0.5618],
                'Seashell': [0.3397, 0.3353],
                'Pale Violet Red': [0.4658, 0.2773],
                'Goldenrod': [0.5136, 0.4444],
                'Aquamarine': [0.2138, 0.4051],
                'Papaya Whip': [0.3591, 0.3536],
                'Saddle Brown': [0.5993, 0.369],
                'Blanched Almond': [0.3695, 0.3584],
                'Khaki': [0.4019, 0.4261],
                'Dark Red': [0.7, 0.2986],
                'Medium Slate Blue': [0.2179, 0.1424],
                'Light Gray': [0.3227, 0.329],
                'Silver': [0.3227, 0.329],
                'Deep Pink': [0.5454, 0.2359],
                'Pale Goldenrod': [0.3751, 0.3983],
                'Coral': [0.5763, 0.3486],
                'Dark Gray': [0.3227, 0.329],
                'Linen': [0.3411, 0.3387],
                'Antique White': [0.3548, 0.3489],
                'Light Yellow': [0.3436, 0.3612],
                'Firebrick': [0.6621, 0.3023],
                'Medium Blue': [0.139, 0.081],
                'Maroon': [0.5383, 0.2566],
                'Dark Khaki': [0.4004, 0.4331],
                'Web Purple': [0.3787, 0.1724],
                'Powder Blue': [0.262, 0.3269],
                'Deep Sky Blue': [0.1576, 0.2368],
                'Orchid': [0.3688, 0.2095],
                'Olive Drab': [0.354, 0.5561]
            }

    # handy functions to the licht object
    def _get_color(self, colorname):
        """ Gets a color from self.colors by name
        :returns: list
        """

        cols = self.colors
        try:
            col = cols[colorname]
            return col
        except KeyError:
            print("Fehler: Farbe %s nicht gefunden" % colorname)
            sys.exit(1)

    def _dimm_percentage(self, percent):
        """ Calculates percentage to hue brightness
        For convenience, user can give brightness in percentage.
        percent: 0-100
        Hue Brightness: 0..254
        :returns: int or False
        """
        try:
            b = float(percent)
            b = 255.0 / 100.0 * b
            b = int(b)
            return b
        except:
            return False

    # core functionality
    def print_all_colors(self):
        """ Print out a list of all available colors
        in colormap. Used for help
        """
        print("Alle verfuegbaren Farben:")
        for x, v in self.colors.iteritems():
            print x + ",",
        return True

    def dim_light(self, percent):
        """ Dim light. Give percentage of brightness.
        """
        b = self._dimm_percentage(percent)
        self.bridge_wrapper.set_group_brightness(b)

    def set_light(self, color, brightness=100, transition=1):
        self.bridge_wrapper.set_group(self._get_color(color), brightness=self._dimm_percentage(brightness), transition=transition)
