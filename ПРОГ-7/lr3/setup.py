from setuptools import setup
from Cython.Build import cythonize

setup(
    name='lr33 app',
    ext_modules=cythonize("lr33.pyx"),
    zip_safe=False,
)