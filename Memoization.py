def memoize(fnc):
    cache = {}
    def inner(*args):
        if args in cache:
            return cache[args]
        cache[args] = fnc(*args)
        return cache[args]


@memoize
def memoized_prime(n):
    for i in range(n, 0, -1):
        if all([i//x!=i/x for x in range(i-1, 1, -1)]):
            return 1




print(memoized_prime(100000))
print(memoized_prime(100000))