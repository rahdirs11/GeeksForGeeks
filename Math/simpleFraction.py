#User function Template for python3

class Solution:
    def fractionToDecimal(self, numerator, denominator):
    # Code here
        output = str(numerator // denominator) + "."

        remainder = numerator % denominator
        recurrance = {}
        if remainder == 0:
            return output + "0"
        while remainder != 0:
            remainder *= 10
            value = remainder // denominator
            if recurrance.get(value, 0) != 0:
                output += '('
                for r in recurrance:
                    output += str(r)
                output += ')'
                return output
            else:
                recurrance[value] = 1
            remainder %= denominator
        for r in recurrance:
            output += str(r)
        return output

print(Solution().fractionToDecimal(int(input()), int(input())))


#{
#  Driver Code Starts
#Initial Template for Python 3
#
# if __name__ == '__main__':
# 	T=int(input())
# 	for i in range(T):
# 		numerator, denominator = input().split()
# 		numerator = int(numerator); denominator = int(denominator)
# 		ob = Solution()
# 		ans = ob.fractionToDecimal(numerator, denominator)
# 		print(ans)
# # } Driver Code Ends
