from cmain import integrate
from pmain import integratePy
import math

print(integrate(0,1,100000))
if __name__ == '__main__':
  import timeit 
  print("Моя функция cython, время",timeit.timeit("integrate(0,1,100000)",globals=globals(),number=100))
  print("Моя функция python, время",timeit.timeit("integratePy(math.cos,0,1)",globals=globals(),number=100))