class Solution:
    # this function will return the number of items that match the rule
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # create a variable to store the index of the item
        index_of_item = -1
        # create a variable to store the result sum
        result_sum = 0
        # check the ruleKey and update the index_of_item
        if ruleKey == "type":
            index_of_item = 0
        elif ruleKey == "color":
            index_of_item = 1
        else:
            index_of_item = 2

        # iterate over the items and check if the item[index_of_item] is equal to ruleValue and add 1 to the result_sum
        for item in items:
            if item[index_of_item] == ruleValue:
                result_sum += 1

        # return the result_sum
        return result_sum
