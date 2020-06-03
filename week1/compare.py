import sys
import numpy as np
import time

def main(n):

    a = np.random.rand(n,n)
    b = np.random.rand(n,n)
    print("a=\n",a)
    print("b=\n",b)
    time1 = time.time()
    product = np.dot(a,b)
    time2 = time.time()
    product2 = calc_product(a,b)
    time3 = time.time()
    printf("np.dot",)
    
    return 0

if __name__ == "__main__":

    args = sys.argv
    if len(args) != 2:
        print("Usage: compare.py <number>", file=sys.stderr)
        sys.exit()

    main(int(args[1]))