import math
import timeit
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from functools import partial

setup = """
from __main__ import integrate
from __main__ import integrate_async
import math
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from functools import partial
"""

def integrate(fn, a, b, countOfSteps=10**6):

    result = 0
    h = 1 / countOfSteps
    while a <= b - h:
        result += (fn(a) + fn(a + h)) / 2 * h
        a += h
    return result

def integrate_async(f, a, b, n_jobs=8, n_iter=10**6):

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        spawn = partial(executor.submit, integrate, f, countOfSteps=n_iter // n_jobs)
        step = (b - a) / n_jobs
        fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
        return sum(f.result() for f in as_completed(fs))

if __name__ == '__main__':

# Multithreading
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=2)', setup=setup, number=100)) # ~ 5.8 sec
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=4)', setup=setup, number=100)) # ~ 2.9 sec
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=6)', setup=setup, number=100)) # ~ 1.9 sec
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=8)', setup=setup, number=100)) # ~ 1.5 sec

# One threaad
    print(timeit.timeit(stmt='integrate(math.cos, 0, 1)', setup=setup, number=100)) # my result 12.5 sec

# Result
    print( integrate(math.cos, 0, 1) )