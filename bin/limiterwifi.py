#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


if __name__ =='__main__':
    dir_of_executable = os.path.dirname(__file__)
    path_to_project_root = os.path.abspath(os.join(dir_of_executable, '..'))
    sys.path.insert(0, path_to_project_root)
    os.chdir(path_to_project_root)

    from limiterwifi.limiterwifi import run # pylit: disable=on-name-in-module
    sys.exit(run())