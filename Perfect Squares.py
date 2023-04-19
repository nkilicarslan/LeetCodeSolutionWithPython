import math
class Solution:
    def numSquares(self, n: int) -> int:
        # create a dp dict up to n and initialize it to 0
        dp_dict = {}

        def recursive_helper(number):
            if number in dp_dict:
                return dp_dict[number]
            if number < 0:
                return math.inf
            elif number == 0:
                return 1
            up_to = int(math.sqrt(number))
            for i in range(up_to,0,-1):
                if number in dp_dict:
                    dp_dict[number] = min(dp_dict[number], recursive_helper(number-i**2) + 1)
                else:
                    dp_dict[number] = recursive_helper(number-i**2) + 1
            return dp_dict[number]
        recursive_helper(n)
        # return the minmum key value in the dp_dict
        return dp_dict[n] -1
a = Solution()
a.numSquares(48)
