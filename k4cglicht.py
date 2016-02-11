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

    parser = ArgumentParser()
    for mode in modes:
        params = mode.get_params()
        try:
            for name, option in params:
                add_arg(parser, name, option)
        except:
            add_arg(parser, params[0], params[1])
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
            print key, value
            modes[key].execute(lightutils, value)




    '''
    args = docopt(__doc__, version='k4cglicht 0.0.2')


    # load modes
    importdir.do("modes", globals())
    modes = [mode for mode in Mode.__subclasses__()]
    mode_name = ''
    arguments = {}
    for key in args.keys():
        if(args[key] and not key.startswith("<")):
            mode_name = key
        elif args[key] and key.startswith('<') :
            arguments[key] = args[key]

    for mode in modes:
        if mode_name in mode.name():
            mode.execute(lu, arguments)
            sys.exit(0)
    print("Mode not found")
    if args["farbe"]:
        #LICHT().set_light(args["<farbname>"])
        print('Bla')
    if args["farben"]:
        LICHT().print_all_colors()
    if args["alarm"]:
        LICHT().alarm()
    if args["blaulicht"]:
        LICHT().blaulicht()
    if args["dimmen"]:
        LICHT().dim_light(args["<prozent>"])
    if args["harmonisch"]:
        d = int(args["<dauer>"])
        LICHT().harmonisch_ausrasten(d)
    if args["normal"]:
        LICHT().default()
    if args["zufall"] or args["alieninvasion"]:
        LICHT().random_colors()
'''
