from eratosthenes import *

primes = []

def initPrimesCache(limit):
    global primes
    primes = SOE(limit)

def prime(num):
    return num in primes

def factorize(num):
    amic = {
        'number'   : num,
        'dividers' : [1],
        'pair'     : 0
    }

    start = 0
    stop = 0
    step = 1

    if num % 2 == 0:
        start = 2
        stop = int( num / 2 )
    else:
        start = 3
        stop = int( num / 3 )
        step = 2

    for divider in range(start, stop + 1, step):
        if num % divider == 0:
            amic['dividers'].append(divider)

    amic['pair'] = sum(amic['dividers'])

    return amic


def amic(num):
    if not prime(num):
        alice = factorize(num)
        if not prime(alice['pair']):
            bob = factorize(alice['pair'])
            if alice['number'] == bob['pair'] and bob['number'] == alice['pair'] and alice['number'] != alice['pair']:
                return { alice['number']: alice['dividers'], bob['number']: bob['dividers'] }
            else:
                return {}
        else:
            return {}
    else:
        return {}