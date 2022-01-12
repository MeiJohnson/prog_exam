from setuptools import setup
from Cython.Build import cythonize

setup(
    name='cython integrate app',
    ext_modules=cythonize("cmain.pyx"),
    zip_safe=False,
)