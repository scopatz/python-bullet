import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
from xdressrc import PACKAGE_NAME, SOURCE_DIR, INCLUDE_DIRS, SOURCE_FILES


def autobuild(file_base):
    return Extension("{}.{}".format(PACKAGE_NAME, file_base),
                     ['{}/{}.cpp'.format(SOURCE_DIR, file_base),
                      "{}/{}.pyx".format(PACKAGE_NAME, file_base)],
                     include_dirs=INCLUDE_DIRS, language="c++")

EXTRAS = [
    Extension("{}.extra_types".format(PACKAGE_NAME),
              ["{}/extra_types.pyx".format(PACKAGE_NAME)],
              include_dirs=INCLUDE_DIRS, language="c++"),
    Extension("{}.stlcontainers".format(PACKAGE_NAME),
              ["{}/stlcontainers.pyx".format(PACKAGE_NAME)],
              include_dirs=INCLUDE_DIRS, language="c++"),
]

setup(
    name=PACKAGE_NAME,
    cmdclass={'build_ext': build_ext},
    ext_modules=[autobuild(f) for f in SOURCE_FILES] + EXTRAS,
    packages=[PACKAGE_NAME]
)
