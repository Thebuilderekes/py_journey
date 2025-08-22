import time
from functools import lru_cache


#! TODO
## find out about functools and lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))


#for i in range(20, 55, 5):
#    start = time.time()
#    result = fibonacci(i)
#    end = time.time()
#    duration = end - start
#    print(f"F({i}) = {result}, time: {duration:.6f} seconds")
