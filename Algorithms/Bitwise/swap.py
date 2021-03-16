'''
Swap 2 numbers without a temporary variable.

We can achieve this by using xor operation
'''

def swap(a: int, b: int) -> list:
	a ^= b
	b ^= a
	a ^= b
	return [a, b]


if __name__ == '__main__':
	a, b = map(int, input().split())
	print('Before swapping, {0} and {1}'.format(a, b))
	a, b = swap(a, b)
	print(f'After swapping, {a} and {b}')

