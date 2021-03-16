'''
All powers of 2 have just one set bit.
So if we perform and operation with the number and number - 1,
we have to get 0.
'''

def powerOf2(number: int):
    return number and not (number & (number - 1))


if __name__ == '__main__':
    number = int(input())
    print(f'{number} is', 'power of 2' if powerOf2(number) else 'not a power of 2')
