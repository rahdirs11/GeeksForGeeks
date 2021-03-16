def unset(n: int, k: int):
	if k <= 0:
		return n
	
	return ~(1 << (k - 1)) & n


def unsetMyMethod(n: int, k: int):
	if k <= 0:
		return n

	t = 1
	while k > 1:
		k -= 1
		t <<= 1
	
	return n ^ t



n, k = map(int, input().split())
print(unset(n, k), unsetMyMethod(n, k), sep="\n")
