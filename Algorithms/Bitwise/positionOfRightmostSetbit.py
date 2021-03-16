def positionOfSetbit(n: int):
	m, position = 1, 1
	while not n & m:
		position += 1
		m <<= 1
	return position


if __name__ == '__main__':
	number = int(input())
	print(f'Position of the rightmost set bit in {number} is {positionOfSetbit(number)}')
