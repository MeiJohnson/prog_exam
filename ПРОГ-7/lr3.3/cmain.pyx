from cython.parallel import prange
from libc.math cimport cos


cpdef double integrate(double a, double b, double n_iter):
  cdef double h = (b-a)/n_iter # step
  cdef double s = 0 # square
  cdef double x = a
  cdef double end = b-h
  while (x <= end):
    s += cos(x)
    x += h
  return h*s
