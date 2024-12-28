#!/usr/bin/env python3
# ------------------------------------------------------------------------------------------------------
# -- __pycache__ nested folder removal from specified root path
# ------------------------------------------------------------------------------------------------------
# ======================================================================================================

import os
import shutil
import subprocess

from quickcolor.color_def import color
from delayviewer.spinner import handle_spinner

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

def remove_pycache_paths(pycachePaths: list):
    print('')
    numRemoved__pycache__Folders = 0
    for idx, item in enumerate(pycachePaths):
        if not os.path.isdir(item):
            print(f" {idx+1:>5}  --> {color.CRED2}No longer a valid path: {color.CWHITE2}{item}{color.CEND}!")

        elif os.path.basename(item) == '__pycache__':
            print(f" {idx+1:>5}  --> Removing {item}")
            shutil.rmtree(item)
            numRemoved__pycache__Folders += 1

        else:
            print(f" {idx+1:>5}  --> {color.CYELLOW2}Warning: {color.CWHITE2}{item} {color.CRED2}is not recognized as {color.CWHITE2}__pycache__{color.CEND}!")

    print(f"\n{color.CGREEN2}Finished removing {color.CWHITE2}{numRemoved__pycache__Folders}{color.CEND} __pycache__ paths!\n")

# ------------------------------------------------------------------------------------------------------

@handle_spinner
def clean_pycache_shell(path: str = None, spinner = None):
    if not path:
        path = os.getcwd()

    if not os.path.isdir(path):
        raise ValueError("Error: Need to specify a valid directory!")

    spinner.start(f"{color.CGREEN2}Looking for {color.CWHITE2}__pycache__{color.CGREEN2} folders under root path {color.CWHITE2}{path}{color.CEND}")
    shellCmd = f"find {path} -type d -name __pycache__"
    action = subprocess.run(shellCmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True)
    intermediate = action.stdout.strip("\n")

    if not len(intermediate):
        spinner.stop(f"{color.CYELLOW}Warning: {color.CRED2}No {color.CWHITE2}__pycache__{color.CRED2} folders found!{color.CEND}")
        return
    findResults = intermediate.split('\n')
    spinner.stop(f'{color.CGREEN2}Found {color.CWHITE2}{len(findResults)}{color.CGREEN2} matches!{color.CEND}')

    remove_pycache_paths(pycachePaths = findResults)

# ------------------------------------------------------------------------------------------------------

@handle_spinner
def clean_pycache_native(path: str = None, spinner = None):
    if not path:
        path = os.getcwd()

    if not os.path.isdir(path):
        raise ValueError("Error: Need to specify a valid directory!")

    spinner.start(f"{color.CGREEN2}Procuring list of {color.CWHITE2}__pycache__{color.CGREEN2} folders under root path {color.CWHITE2}{path}{color.CEND}")
    listOfPycacheDirs = []
    for rootDir, dirlist, filelist in os.walk(path, topdown=False):
        listOfPycacheDirs.extend([ os.path.join(rootDir, elem) for elem in dirlist if os.path.basename(elem) == '__pycache__' ])

    if not len(listOfPycacheDirs):
        spinner.stop(f"{color.CYELLOW}Warning: {color.CRED2}No {color.CWHITE2}__pycache__{color.CRED2} folders found!{color.CEND}")
        return
    spinner.stop(f'{color.CGREEN2}Found {color.CWHITE2}{len(listOfPycacheDirs)}{color.CGREEN2} matches!{color.CEND}')

    remove_pycache_paths(pycachePaths = listOfPycacheDirs)

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

