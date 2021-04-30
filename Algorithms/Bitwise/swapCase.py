def swapCase(string: str):
	newString = str()
	for s in string:
		newString += chr(ord(s) ^ 32)

	return newString


while True:
	try:	print(swapCase(input()))
	except:
		print('Enter valid input!!')
		continue
	else:
		break
