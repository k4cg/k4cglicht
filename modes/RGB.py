from mode import Mode
from colormath.color_objects import XYZColor, sRGBColor
from colormath.color_conversions import convert_color
import re

class RGB(Mode):

    @staticmethod
    def get_params():
        return('rgb', 'rgb_in_hex')

    @staticmethod
    def execute(light_utils, argument=None):
        hex_pattern = '^[0-9a-fA-F]{6}|#[0-9a-fA-F]{6}$'
        match = re.search(hex_pattern, argument)
        hex_value = match.group(0).replace('#', '')
        rgb_hex = tuple([hex_value[i:i+2] for i in range(0, len(hex_value), 2)])
        red = rgb_hex[0]
        green = rgb_hex[1]
        blue = rgb_hex[2]

        red, green, blue = int(red, 16), int(green, 16), int(blue, 16)
        rgb = sRGBColor(red, green, blue)
        xyz = convert_color(rgb, XYZColor)
        x = xyz.xyz_x
        y = xyz.xyz_y
        z = xyz.xyz_z
        final_x = x / (x + y + z)
        final_y = y / (x + y + z)
        xy = [final_x , final_y]
        light_utils.set_color(xy)
