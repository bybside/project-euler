def main():
    for i in range(10):
        print(f"smallest multiple for range 1..{i}: {smallest_multiple(i)}")

# time complexity: O(n) where n is max factor
# bug: gets common multiple but not lcm
def smallest_multiple(max_fact: int):
    n = 1
    for i in range(max_fact, 0, -1):
        if n % i != 0:
            n *= i
    return n

main()
