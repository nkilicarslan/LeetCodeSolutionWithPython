class Solution:
    # this function will return all the possible combinations of the n pairs of parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        # create a list to store the result
        result_arr = []
        # create a function to generate the combinations recursively
        def recursive_helper(open_parenthes, close_parenthes, result_arr, instant_combination):
            # if the number of the open parentheses is greater than the number of the close parentheses
            if close_parenthes == 0:
                # if it is valid append it to the result_arr
                result_arr.append(instant_combination)
                # return (the base case)
                return
            # if the number of the open parentheses is greater than 0
            if open_parenthes != 0:
                # call the recursive function with open_parenthes-1
                recursive_helper(open_parenthes-1, close_parenthes, result_arr, instant_combination + '(')
            # call the recursive function with close_parenthes-1
            if close_parenthes > open_parenthes:
                # call the recursive function with close_parenthes-1
                recursive_helper(open_parenthes, close_parenthes-1, result_arr, instant_combination + ')')
        # call the recursive function with n, n, result_arr and an empty string
        recursive_helper(n, n, result_arr, '')
        # return the result_arr
        return result_arr
