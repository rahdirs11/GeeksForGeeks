'''
RUSSIAN PEASANT ALGORITHM
The idea is to double the first number and half the second, until second doesnt become 0,
AND add first number to the result when second is odd
'''

def multiply(a: int, b: int):
	res = 0
	while b > 0:
		if b & 1:	# checking if it is odd
			res += a
		a <<= 1
		b >>= 1
	return res


if __name__ == '__main__':
	a, b = map(int, input().split())
	print(f'{a} x {b} without multipliication opeator is {multiply(a, b)}')

