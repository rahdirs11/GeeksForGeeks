'''
Check if a number has bits in alternate positions i.e. 
set bits in alternate positions

15 -> 1111 -> NO
2 -> 10 -> YES
5 -> 101 -> yes
'''

def simpleApproach(n: int):
	previous = n % 2
	n >>= 1
	while n > 0:
		current = n % 2
		if current == previous:
			return False
		previous = current
		n >>= 1
	return True

