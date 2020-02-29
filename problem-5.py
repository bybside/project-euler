def main():
    n = 20
    print(f"smallest multiple for range 1..{n}: {get_lcm(n)}")

def get_lcm(max_factor: int):
    if max_factor <= 1:
        return max_factor
    lcm = 1
    fact_counts = count_factors(max_factor)
    for k, v in fact_counts.items():
        lcm *= (k**v)
    return lcm
	
def count_factors(max_factor: int):
	max_counts = {}
	for i in range(1, max_factor + 1):
		for fact, count in prime_fact(i).items():
			if count > max_counts.get(fact, 0):
				max_counts[fact] = count
	return max_counts
				
def prime_fact(n: int):
	"""
	pf {factor: count}
	"""
	pf = {}
	while n % 2 == 0:
		pf[2] = pf.get(2, 0) + 1
		n //= 2
	i = 3
	while i <= n**(1/2):
		while n % i == 0:
			pf[i] = pf.get(i, 0) + 1
			n //= i
		i += 2
	if n > 2:
		pf[n] = 1
	return pf

main()
