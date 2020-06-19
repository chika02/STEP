import sys
import numpy as np
import time

def array_generator(n):
    array = np.random.rand(n,n)
    return array


def product_py(A,B,n):
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k]*B[k][j] for k in range(n))
    return C


def product_np(A,B):
    product = np.dot(A,B)
    return product

def measure_time_py(n):

    A = array_generator(n)
    B = array_generator(n)
    t1 = time.time()
    C = product_py(A,B,n)
    t2 = time.time()

    return (t2-t1)*10**6

def measure_time_np(n):

    A = array_generator(n)
    B = array_generator(n)
    t1 = time.time()
    C = product_np(A,B)
    t2 = time.time()

    return (t2-t1)*10**6

if __name__ == "__main__":

    path1 = "time_py.csv"
    path2 = "time_np.csv"
    max_n = 100
    m = 10
    ave = 0
    with open (path1, mode="w") as f:
        for n in range(max_n):
            for j in range(m):
                ave += measure_time_py(n)*1.0/m
            f.write("%d  %lf\n" %(n, ave))
    ave = 0
    with open (path2, mode="w") as f:
        for n in range(max_n):
            for j in range(m):
                ave += measure_time_np(n)*1.0/m
            f.write("%d  %lf\n" %(n, ave))
