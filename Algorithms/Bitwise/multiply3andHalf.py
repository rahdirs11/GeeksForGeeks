'''
Given an integer, wirte a function that multiplies x with 3.5
and returns the integer result. You are not allowed to sue %. /. or *
'''

'''
Approach is, to use 2x + x + x / 2.
To get 2x, we left shift by one.
To get x/2, we right shift by one.
'''

def multiply3_5(x: int):
    return (x << 1) + x + (x >> 1)


if __name__ == '__main__':
    n = int(input())
    print(f'{n} x 3.5 => {multiply3_5(n)}')
