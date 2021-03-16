def swapNibble(number: int) -> int:
	return (number & 0x0f) << 4 | (number & 0xF0) >> 4


print(swapNibble(int(input())))

