def main():
    n = 35
    print(sum_even_fib(n))

# time complexity: O(n)
def sum_even_fib(n: int):
    """
    sum a range of even fibonacci values
    """
    s = 0
    cache = {}
    for i in range(1, n + 1):
        fib_val = fib_util(i, cache)
        if fib_val > 4000000:
            break
        if fib_val % 2 == 0:
            s += fib_val
    return s

def fib_util(n: int, cache: dict):
    """
    return the nth fibonacci value;
    caching so each value is computed only once
    """
    if n <= 2:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib_util(n - 1, cache) + fib_util(n - 2, cache)
    return cache[n]
    
main()
