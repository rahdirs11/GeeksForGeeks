'''
To multiply a number with 7, we multiply the number with 8, and subtract it with the number itself.
Left shift by 3 is multiplying with 8, and then we subtract the product with the number itself.
'''


def multiply(number: int) -> int:
    return (number << 3) - number


if __name__ == '__main__':
    number = int(input())
    print(f'{number} * 7 = {multiply(number)}')
