# Написание программы для численного интегрирования площади под кривой.

import math
import concurrent.futures as ftres
from functools import partial



def integratePy(f, a, b, *, n_iter=10**6):
  h = (b-a)/n_iter # step
  s = 0 # square
  x = a
  end = b-h
  while (x <= end):
    s = s+f(x)
    x += h
  return float(h*s)

def integrate_async(f, a, b, *, n_jobs=2, n_iter=10**6):

    # из futures необходимо импортировать и оценить время выполнения интегрирования
    # с помощью процессов, а потом потоков.
    # используйте высокоуровневые классы для этого, см.
    # https://docs.python.org/3/library/concurrent.futures.html
    # в этом месте необходимо создать объекты этих классов, при этом количество потоков/процессов равняется количеству n_jobs.
  with ftres.ThreadPoolExecutor(max_workers=n_jobs) as executor:
    spawn = partial(executor.submit, integratePy, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return sum(f.result() for f in ftres.as_completed(fs))

if __name__ == '__main__':
  import timeit 
  print("Моя функция",timeit.timeit("integratePy(math.cos,0,1)",globals=globals(),number=100))
  print("функция с 2 потоками",timeit.timeit("integrate_async(math.cos,0,1)",globals=globals(),number=100))
  print("функция с 4 потоками",timeit.timeit("integrate_async(math.cos,0,1,n_jobs=4)",globals=globals(),number=100))
  print("функция с 6 потоками",timeit.timeit("integrate_async(math.cos,0,1,n_jobs=6)",globals=globals(),number=100))
  # print(integrate_async(math.cos,3,7,n_jobs=6))

