import random
import numpy as np
import time

def main():
    n_A = int(input('Введите размер n матрицы A '))
    m_A = int(input('Введите размер m матрицы A '))
    n_B = int(input('Введите размер n матрицы B '))
    m_B = int(input('Введите размер m матрицы B '))
    if(m_A == n_B):
        A = np.array([[random.randint(1, 10) for j in range(m_A)] for i in range(n_A)])
        print(A)
        B = np.array([[random.randint(1, 10) for j in range(m_B)] for i in range(n_B)])
        print(B)
        C = A.dot(B)
        print(C)
    else:
        print('Невозможно произвести умножение матриц заданного размера')
    

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
