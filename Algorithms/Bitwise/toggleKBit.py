def toggle(n: int, k: int):
	return n ^ (1 << (k - 1))


print(toggle(int(input())))