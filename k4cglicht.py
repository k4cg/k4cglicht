#!/usr/bin/env python

def load_modes():
    importdir.do("modes", globals())
    modes = {}
    for mode in Mode.__subclasses__():
        params = mode.get_params()
        try:
            for name, option in params:
                modes[name] = mode
        except:
            modes[params[0]] = mode
    return modes

def init_parser(modes):
    def add_arg(parser, name, option):
        if not option:
            parser.add_argument('--' + name, action='store_true')
        else:
            parser.add_argument('--' + name, metavar=option)

    parser = ArgumentParser(prog='k4cglicht.py')
    for mode in modes:
        params = mode.get_params()
        try:
            for name, option in params:
                add_arg(parser, name, option)
        except:
            add_arg(parser, params[0], params[1])
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser

import sys
import json
from argparse import ArgumentParser
from vendor import importdir
from mode import Mode
from lightutils.LightUtils import LightUtils

if __name__ == '__main__':
    modes = load_modes()
    parser = init_parser(set(modes.values()))
    args = parser.parse_args()

    config = []
    with open('config.json') as configFile:
        config = json.load(configFile)
    lightutils = LightUtils(config)

    for key, value in args.__dict__.iteritems():
        if value:
            modes[key].execute(lightutils, value)
