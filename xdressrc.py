from __future__ import print_function
import os
import numpy as np
from xdress.utils import apiname


# config
PACKAGE_NAME = 'bullet'
SOURCE_DIR = os.path.join(os.getcwd(), 'src')
EXCLUDES = [
    'DX11', 'OpenCL', 'BulletMultiThreaded', # General excludes for compilation reasons (Linux vs Windows, etc.)
    'Vehicle', 'btAlignedObjectArray', 'btContactConstraint', # Excluded because they were causing xdress problems
    'Gimpact', 'Featherstone', 'vectormath', 'MiniCL', 'Bullet-C-Api.h', 'BulletSoftBody', # Just to simplify things while I'm getting it to work
    ]
def contains_excluded(path):
    for e in EXCLUDES:
        if e in path:
            return True
    return False
INCLUDE_DIRS = [s[0] for s in os.walk(SOURCE_DIR) if not contains_excluded(s)] + [np.get_include()]
ALL_FILES = []
[ALL_FILES.extend(os.path.join(d[0], f) for f in d[2]) for d in os.walk(SOURCE_DIR)]
for f in ALL_FILES[:]:
    if contains_excluded(f):
        ALL_FILES.remove(f)

SOURCE_FILES = [f for f in ALL_FILES if f.endswith('.cpp')]
INC_FILES = [f for f in ALL_FILES if f.endswith('.h')]

# execution
includes = [SOURCE_DIR]
package = PACKAGE_NAME     # top-level python package name
packagedir = PACKAGE_NAME  # location of the python package
# TODO: The incfiles is blank (for now)
API_NAMES = [apiname('*', (f, f.replace('.cpp', '.h')), incfiles=[], language="c++") for f in SOURCE_FILES]

extra_types = 'extra_types'
stlcontainers = []
classes = API_NAMES
functions = API_NAMES

