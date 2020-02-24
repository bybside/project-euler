def main():
    n = 600851475143
    print(largest_prime_factor(n))

def largest_prime_factor(n: int):
    pf = []
    # halve n until odd
    while n % 2 == 0:
        pf.append(2)
        n //= 2
    # find all odd prime factors
    i = 3
    while i < n**(1/2):
        while n % i == 0:
            pf.append(i)
            n //= i
        i += 2
    # if n is a prime number > 2
    # full factorization will not
    # be accomplished by above code
    if n > 2:
        pf.append(n)
    return pf[-1]

main()
