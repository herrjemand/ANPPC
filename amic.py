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
    # Fermat primality test
    prime = lambda p: True if p != 0 and 571 ** (p - 1) % p == 1 else False

    if not prime(num):
        alice = factorize(num)
        if not prime(alice['pair']):
            bob = factorize(alice['pair'])
            if alice['number'] == bob['pair'] and bob['number'] == alice['pair']:
                return { alice['number']: alice['dividers'], bob['number']: bob['dividers'] }
            else:
                return None
        else:
            return None
