cache = {0:0, 1:1}

def optimized(n, cache):
    if n not in cache:
        cache[n] = optimized(n-1, cache) + optimized(n-2, cache)
    return cache[n]
