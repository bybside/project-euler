def main():
    n = 10001
    p_num = nth_prime(n)
    print(f"prime number #{n}: {p_num}")

# time complexity: O(n^2)
def nth_prime(n: int):
    """
    returns the nth prime number
    """
    if n <= 0:
        return -1
    # start testing numbers at 3;
    # test until nth prime is reached
    p_count = 1
    p_num = 2
    i = 3
    while p_count < n:
        if is_prime(i):
            p_num = i
            p_count += 1
        i += 1
    return p_num
       
def is_prime(n: int):
    if n % 2 == 0:
        return False
    for j in range(3, (n // 2) + 1, 2):
        if n % j == 0:
            return False
    return True

main()
