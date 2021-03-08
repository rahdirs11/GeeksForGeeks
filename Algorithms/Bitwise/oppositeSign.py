'''
Given two signed integers, write a function that return true if the signs of
given integers are different, otherwise return false.
'''

'''
The idea here is to check the MSB,
which is -> 1 if number is negative
         -> 0 if number is positive
So, we perform bitwise xor operation.
This will return a negative number if
the signs are different,else return
a positive number.
(xor -> same numbers results in false
     -> differennt numbers results in true
     -> even parity!)
'''


def oppositeSign(x: int, y: int) -> bool:
    return (x ^ y) < 0


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(f'{a} and {b} have', 'opposite signs' if oppositeSign(a, b) else 'same sign')
