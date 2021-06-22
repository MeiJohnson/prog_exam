import random
import numpy as np
import time

def main():
    A = np.matrix('1 2 3; 4 5 6')
    B = np.matrix('7 8; 9 1; 2 3')
    C = A.dot(B)
    print(C)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
