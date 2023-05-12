class Solution:
    # this function will return the matrix with the given conditions
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # create a result array
        result_array = [[]]
        # iterate over the nums
        for num in nums:
            # create a variable to check if the number is appended to the result array or not
            appended_or_not = False
            # iterate over the result array
            for list in result_array:
                # if the number is not in the list, append the number to the list and update the appended_or_not variable
                if num not in list:
                    list.append(num)
                    appended_or_not = True
                    break
            # if the number is not appended to the result array, append the number to the result array
            if appended_or_not == False:
                result_array.append([num])
        # return the result array
        return result_array
