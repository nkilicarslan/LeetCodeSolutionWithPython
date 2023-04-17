class Solution:
    # this function will return a list of booleans where the ith element is true if the ith kid has the greatest number of candies
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find the maximum number of candies
        maximum_candie = max(candies)
        # create a list to store the result
        result_list = []

        # iterate over the candies list
        for candie in candies:
            # if the sum of the current candy and the extra candies is greater than or equal to the maximum candies, append True to the result list
            if candie + extraCandies >= maximum_candie:
                result_list.append(True)
            # otherwise append False to the result list
            else:
                result_list.append(False)

        return result_list
