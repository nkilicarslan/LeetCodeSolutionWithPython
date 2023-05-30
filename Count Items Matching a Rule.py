class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index_of_item = -1
        result_sum = 0
        if ruleKey == "type":
            index_of_item = 0
        elif ruleKey == "color":
            index_of_item = 1
        else:
            index_of_item = 2

        for item in items:
            if item[index_of_item] == ruleValue:
                result_sum += 1

        return result_sum

