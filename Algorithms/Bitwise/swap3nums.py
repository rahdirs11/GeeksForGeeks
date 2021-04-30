'''
Swap three numbers without using a temporary variable
'''

'''
We can either use arithmetic operators
			OR
Use xor
'''

def swap(a, b, c):
	a = a ^ b ^ c
	b = a ^ b ^ c
	c = a ^ b ^ c
	a = a ^ b ^ c
	return a, b, c


a, b, c = 10, 20, 30
print(swap(a, b, c))