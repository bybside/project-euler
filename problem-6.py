def main():
    print(sum_square_difference(100))

# time complexity: O(n)
def sum_square_difference(u_bound: int):
    """
    find the sum square difference for
    a range of numbers (1..u_bound)
    
    note: the squared sum of a range of
    numbers = sum of cubes for a range
    of numbers
    """
    s1 = 0
    for i in range(2, u_bound + 1):
        s1 += (i**3) - (i**2)
    return s1

main()
