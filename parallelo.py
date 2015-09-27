from amic import *
from time import time
import multiprocessing
from multiprocessing import Pool
start = time()
z = ''
poolsize = multiprocessing.cpu_count()

def f(x):
    if not prime(x):
        return x

with Pool(poolsize) as p:
    z = [x for x in p.map(f,[i for i in range(0, 30000)]) if x is not None]

stop = time()
print(stop - start)
