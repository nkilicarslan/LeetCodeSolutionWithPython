class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp_result = [1] * 5
        for i in range(1,n):
            for j in range(3,-1,-1):
                dp_result[j] = dp_result[j] + dp_result[j+1]
        sum = 0
        for i in range(5):
            sum += dp_result[i]
        return sum