'''
Approach is simple. If we perform modulus of x by n, we get the number of bits
to the right of the set bit of n.
5(101) % 2(10) = 1(1)
6(110) % 4(100) = 2(10)
'''


def modPow2(a: int, b: int):
    return a & (b - 1)
    # b - 1 will have all the btis flipped from the rightmost set bit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(modPow2(a, b))
