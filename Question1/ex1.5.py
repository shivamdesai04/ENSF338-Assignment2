import timeit
import matplotlib.pyplot as plt

cache = {0:0, 1:1}


def original_fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return original_fibonacci(num-1) + original_fibonacci(num-2)

def optimized(n, cache):
    if n not in cache:
        cache[n] = optimized(n-1, cache) + optimized(n-2, cache)
    return cache[n]

optimized_times = []
non_optimized_times = []
for i in range(36):
    elapsed_time_optimized = timeit.timeit(lambda: optimized(i, cache),number= 1)
    optimized_times.append(elapsed_time_optimized)
    elapsed_time_non_optimized = timeit.timeit(lambda: original_fibonacci(i), number= 1)
    non_optimized_times.append(elapsed_time_non_optimized)


plt.plot(optimized_times,label="Optimized Fibonacci")
plt.plot(non_optimized_times,label="Original Fibonacci")
plt.xlabel("nth Fibonacci Number Calculated")
plt.ylabel("Time (seconds)")
plt.xticks(range(36))
plt.legend()
plt.show()

