class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result_array = [[]]
        for num in nums:
            appended_or_not = False
            for list in result_array:
                if num not in list:
                    list.append(num)
                    appended_or_not = True
                    break
            if appended_or_not == False:
                result_array.append([num])
        return result_array