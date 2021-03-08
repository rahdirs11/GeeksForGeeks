'''
For any n, n - 1 will have all the bits after the rightmost 1, flipped.
So if we perfrom n & n - 1, we can unset the rightmost bit.
'''

def unset(x: int) -> int:
    return x & (x - 1)


if __name__ == '__main__':
    n = int(input())
    print(f'After unsetting, {n} = {unset(n)}')
