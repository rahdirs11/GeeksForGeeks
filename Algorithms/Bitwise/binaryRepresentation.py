def repeatedDiv(n: int):
	if n == 0:
		return
	repeatedDiv(n >> 1)
	print(1 if n & 1 else 0, end='')


repeatedDiv(int(input()))
