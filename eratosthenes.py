def SOE(limit):
    '''Sieve of Eratosthenes'''
    net = [ n for n in range(0, limit) ]

    i = 0

    while i < limit:

        if net[i] > 1:

            p = net[i]
            j = 2
            while j * p < limit:
                net[j * p] = 0
                j += 1


        i += 1

    return [n for n in net if n > 1]