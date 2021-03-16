import powerOf2

def position(n: int) -> int:
	if not powerOf2.powerOf2(n):
		return -1
	position = 1
	while n > 0 and n ^ 1:
		n >>= 1
		position += 1
	return position


print(position(int(input())))
		
