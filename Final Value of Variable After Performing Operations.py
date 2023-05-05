class Solution:
    # this function will return the final value of the variable after performing the operations
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # create a variable to store the final result
        final_result = 0
        # iterate over the operations list
        for operation in operations:
            # if the operation is '--X' or 'X--', decrement the final_result by 1
            if operation[0] == '-' or operation[-1] == '-':
                final_result -= 1
            # otherwise if the operation is '++X' or 'X++', increment the final_result by 1
            else:
                final_result += 1
        # return the final_result
        return final_result
