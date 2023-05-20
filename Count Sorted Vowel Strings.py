class Solution:
    # this function will return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
    def countVowelStrings(self, n: int) -> int:
        # create a dp array to store the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
        dp_result = [1] * 5
        # iterate over the n - 1 times
        for i in range(1,n):
            # iterate over the dp_result array from right to left
            for j in range(3,-1,-1):
                # update the dp_result array
                dp_result[j] = dp_result[j] + dp_result[j+1]
        # create a variable to store the sum of the dp_result array
        sum = 0
        # iterate over the dp_result array and add the elements to the sum
        for i in range(5):
            sum += dp_result[i]
        # return the sum
        return sum
