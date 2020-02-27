def main():
    print(largest_palindrome(3))

# time complexity: O(n^2) where n is the
# number of digits in each desired factor
def largest_palindrome(fact_length: int):
    n = 0
    u_bound = (10**fact_length)-1
    l_bound = 10**(fact_length-1)
    for i in range(u_bound, l_bound, -1):
        for j in range(i, l_bound, -1):
            val = i*j
            if val > n and is_palindrome(val):
                n = val
    return n

# there is a more efficient way to
# check if numbers are palindromes
def is_palindrome(n: int):
    return str(n) == str(n)[::-1]

main()
