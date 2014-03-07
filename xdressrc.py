from __future__ import print_function
import os
import numpy as np
from xdress.utils import apiname


# config
PACKAGE_NAME = 'bullet'
SOURCE_DIR = os.path.join(os.getcwd(), 'src')
INCLUDE_DIRS = [s[0] for s in os.walk(SOURCE_DIR)] + [np.get_include()]
ALL_FILES = []
[ALL_FILES.extend(os.path.join(d[0], f) for f in d[2]) for d in os.walk(SOURCE_DIR)]
EXCLUDES = ['DX11', 'OpenCL', 'BulletMultiThreaded', 'btAlignedObjectArray']
def contains_excluded(path):
    for e in EXCLUDES:
        if e in path:
            return True
    return False
SOURCE_FILES = [f for f in ALL_FILES if f.endswith('.cpp') and not contains_excluded(f)]
INC_FILES = [f for f in ALL_FILES if f.endswith('.h') and not contains_excluded(f)]

OBJ_ARRAY = os.path.join(SOURCE_DIR, 'LinearMath', 'btAlignedObjectArray.h')

# execution
includes = [SOURCE_DIR]
package = PACKAGE_NAME     # top-level python package name
packagedir = PACKAGE_NAME  # location of the python package
API_NAMES = [apiname('*', (f, f.replace('.cpp', '.h')), incfiles=INC_FILES, language="c++") for f in SOURCE_FILES]

extra_types = 'extra_types'

stlcontainers = [
    ('vector', 'str'),
    ('set', 'uint'),
    ('map', 'int', 'float'),
    ]

classes = API_NAMES
functions = API_NAMES

