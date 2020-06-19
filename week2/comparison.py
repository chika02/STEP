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


if __name__ == "__main__":

    args = sys.argv
    if len(args) != 2:
        print("usage: python comparison.py <number>",file = sys.stderr)
        sys.exit(1)
    if not args[1].isdigit():
        print("invalid character detected",file = sys.stderr)
        sys.exit(1)
    n = int(args[1])

    A = array_generator(n)
    B = array_generator(n)
    t1 = time.time()
    C = product_py(A,B,n)
    t2 = time.time()
    D = product_np(A,B)
    t3 = time.time()

    path1 = "time_py.csv"
    path2 = "time_np.csv"
    with open (path1, mode="a") as f:
        f.write("%d  %lf\n" %(n, (t2-t1)*10**6))
    with open (path2, mode="a") as f:
        f.write("%d  %lf\n" %(n, (t3-t2)*10**6))

