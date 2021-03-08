'''
All powers of 4, have even number of unset bits, and just one set bit.
Count number of unset bits, and check if it is even.
'''
def isPowerOf4(x: int) -> int:
    count = 0
    if x and not (x & (x - 1)):
        while x > 1:
            count += 1
            x >>= 1

        return count % 2 == 0
    return False

'''
Using log operation, we can find if a number is a power of 4 or not
'''
def isPowerOf4log(x: int) -> bool:
    from math import log2, trunc
    result = log2(x) / log2(4)
    return result - trunc(result) == 0

if __name__ == '__main__':
    n = int(input())
    print(isPowerOf4(n))
    print(isPowerOf4log(n))
