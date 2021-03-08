'''
WAP to add one to a given number. The use of operators like +, -, /, *, ++, --
are not allowed
'''


'''
On adding one to any number, the bits after the rigthmost 0 are flipped, and the
bit itself(rightmost 0 before flipping), is made a set bit.
In order to achieve this, we use xor to flip the bits until the and operation is
false -> until we hit the rightmost unset bit before flipping
'''
def addOne(x: int) -> int:
    '''
    Flipping bits approach
    '''
    m = 1
    while x & m:
        x ^= m
        m <<= 1
    x ^= m
    return x

'''
Another approach is to use 2's complement.
Negation of x (~x) is -(x + 1), so we use -(~x)
'''


def addOne2(x: int) -> int:
    '''
    2's complement approach
    '''
    return -(~(x))

if __name__ == '__main__':
    n = int(input())
    print(f'{n} + 1 => {addOne2(n)}')
