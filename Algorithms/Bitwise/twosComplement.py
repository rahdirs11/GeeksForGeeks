'''
A = 0111
A' = 1001

B = 1100
B' = 0011 + 1 -> 0100

1100
0100


A = 0100
A' = 1011 + 1 -> 1100

'''

def twosComplement(binary: str):
	newBinary = str()
	flip = binary[-1] == '1'

	for i, b in enumerate(binary[: -1]):
		if flip:
			newBinary += '1' if b == '0' else '0'
		else:
			if i == 0:
				newBinary += '1' if b == '0' else '0'
			else:
				newBinary += b
	newBinary += binary[-1]
	return newBinary


print(twosComplement('0111'))
print(twosComplement('0100'))
print(twosComplement('1100'))
