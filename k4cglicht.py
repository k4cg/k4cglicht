#!/usr/bin/env python
""" k4cglicht 0.0.2

Usage:
  k4cglicht farbe <farbname>
  k4cglicht farben
  k4cglicht alarm
  k4cglicht blaulicht
  k4cglicht alieninvasion
  k4cglicht dimmen <prozent>
  k4cglicht normal
  k4cglicht zufall <dauer>
  k4cglicht harmonisch ausrasten <dauer>
  k4cglicht harmonisch

Options:
  -h --help     HILFE!
  --version     FICKENDE VERSION!

"""

import sys
import random
import json
from docopt import docopt
from vendor import importdir
from mode import Mode
from lightutils.LightUtils import LightUtils

if __name__ == '__main__':
    args = docopt(__doc__, version='k4cglicht 0.0.2')

    config = []
    with open('config.json') as configFile:
        config = json.load(configFile)
    lu = LightUtils(config)

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
'''
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
