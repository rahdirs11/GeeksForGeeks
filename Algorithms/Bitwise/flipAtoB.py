'''
Count number of bits needed to flip, to convert a to b.
'''


'''
011
001

010


eg: 10, 20 => output
10 -> 01010
20 -> 10100
If we flip 4 bits, we get 20 from 10

By performing a ^ b, and counting the number of set bits, we get the output.
'''

def countFlips(a: int, b: int):
    xor = a ^ b
    count = 0
    while xor > 0:
        count += 1
        xor &= xor - 1

    return count


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(f'We need to flip {countFlips(a, b)} bits to convert {a} to {b}')
