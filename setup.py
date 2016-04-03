# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize
import numpy


setup(name='pyEPABC', 
    ext_modules = cythonize(Extension("testDDM_C", 
                                      ["examples/testDDM_C.pyx"],
                                      include_dirs=["src", numpy.get_include()],
                                      libraries=["DDMsampler"],
                                      library_dirs=["lib"], 
                                      runtime_library_dirs=["lib"]
                                      )),
    packages=['pyEPABC']
)