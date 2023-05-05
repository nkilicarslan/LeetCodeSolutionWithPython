class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_result = 0
        for operation in operations:
            if operation[0] == '-' or operation[-1] == '-':
                final_result -= 1
            else:
                final_result += 1
        return final_result