'''
To find the only element that occurs odd number of times,
we can perform xor of all the elements of the array.
Since xor of same numbers is 0, and every element occurs even number of
times, the final result will be the only element which occurs odd number of 
times!

Another way to do this problem would be to use a hash-map/dictionary.
But this would be of time complexity - O(n) and space complexity - O(n)
'''

def oddOccurring(arr: list) -> int:
    xor = arr[0]
    for a in arr[1: ]:
        xor ^= a

    return xor


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print('The number which occurs odd number of times is {}'.format(oddOccurring(arr)))
