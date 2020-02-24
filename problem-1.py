def main():
    n = 1000
    print(get_nums(n))

# time complexity: O(n)
def get_nums(n: int):
    """
    sum all natural numbers below n that
    are multiples of 3 or 5
    """
    s = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            s += i
    return s

main()
