from amic import *
from time import time
import multiprocessing, json
from multiprocessing import Pool

limit = 10 ** 6

print('Searching for amicable numbers within next ', limit)

start = time()

poolsize = multiprocessing.cpu_count()

amicables = {}

initPrimesCache(limit)

with Pool(poolsize) as p:
    temp = p.map(amic, [i for i in range(0, limit)])

    for am in [t for t in temp if t != {}]:
        amicables.update(am)


stop = time()
print(stop - start)

print('Found', len(amicables), 'amicable numbers')

with open('cache.' + str(limit) + '.json', 'w') as w:
    w.write(json.dumps(amicables))
