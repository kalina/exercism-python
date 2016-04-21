
def sieve(limit):
    numbers = [True for x in range(limit+1)]
    numbers[0] = False
    numbers[1] = False

    primes = []

    #bad nested loop - should refactor this
    for idx, item in enumerate(numbers):
        print idx
        if item:
            primes.append(idx)
            for idx2, val in enumerate(numbers):
                if numbers[idx2]:
                    numbers[idx2] = idx2 % idx
    return primes
