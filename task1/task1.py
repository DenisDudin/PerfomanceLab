import numpy as np
import sys

if __name__ == '__main__':
    file = sys.argv[1]
    a = []

    with open(file, 'r') as f:
        a = [int(line) for line in f.readlines()]
    print("%.2f"%np.percentile(a, 90))
    print("%.2f"%np.median(a))
    print("%.2f"%np.max(a))
    print("%.2f"%np.min(a))
    print("%.2f"%np.average(a))
