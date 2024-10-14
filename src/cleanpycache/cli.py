#!/usr/bin/env python3
# ------------------------------------------------------------------------------------------------------
# -- CLI for cleaning __pycache__ nested folders from specified root path
# ------------------------------------------------------------------------------------------------------
# ======================================================================================================

# PYTHON_ARGCOMPLETE_OK
import argcomplete, argparse

import os
import sys

from quickcolor.color_def import color
from showexception.showexception import exception_details

from .cleanpycache import clean_pycache_shell
from .cleanpycache import clean_pycache_native

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

def cli():
    try:
        parser = argparse.ArgumentParser(
                    description=f'{"-." * 3}  {color.CBLUE2}Cleaning {color.CWHITE2}__pycache__{color.CYELLOW2} folders!{color.CEND}',
                    epilog='-.' * 40)

        p_path = parser.add_argument('path', nargs='?', default=None,
                metavar="<path>", help="absolute root path to start clearing")

        p_runType = parser.add_argument('-r', '--runtype', choices=['native', 'shell'],
                default='native', metavar='<runtype>',
                help="run type for clearing __pycache__ folders (shell cmds or native python)")

        argcomplete.autocomplete(parser)
        args = parser.parse_args()
        # print(args)

        if args.runtype == 'native':
            clean_pycache_native(path=args.path)

        elif args.runtype == 'shell':
            clean_pycache_shell(path=args.path)

    except Exception as e:
        exception_details(e, "Clean __pycache__ CLI")

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

