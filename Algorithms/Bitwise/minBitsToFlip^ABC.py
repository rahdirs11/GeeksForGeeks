def minBits(a: int, b: int, c: int) -> int:
	xor = a ^ b ^ c
	count = 0
	while xor > 0:
		if xor & 1:
			count += 1

		xor //= 2

	return count

print(minBits(6, 5, 1))