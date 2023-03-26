class Solution:
    def isValid(self, s: str) -> bool:
        # create stack to keep track of the paranthesis
        stack_list = []
        # iterate over the string
        for i in s:
            # if char one of them ('(' or '{' or '[') push to the stack
            if i == '(' or i == '{' or i == '[':
                stack_list.append(i)
            # if char one of them (')' or '}' or ']')
            else:
                # check the stack is empty or not
                if len(stack_list) == 0:
                    return False
                # pop the last value of the stack
                popped_element = stack_list.pop()
                # if these two char are matched, continue
                if (popped_element == '(' and i == ')') or (popped_element == '{' and i == '}') or (
                        popped_element == '[' and i == ']'):
                    continue
                # if these two char are not matched return false
                else:
                    return False
        # if the stack is empty return true
        if len(stack_list) == 0:
            return True
        # otherwise return false
        else:
            return False
    # this function will return all the possible combinations of the n pairs of parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        # create a list to store the result
        result_arr = []
        # create a function to generate the combinations recursively
        def recursive_helper(open_parenthes, close_parenthes, result_arr, instant_combination):
            # if the number of the open parentheses is greater than the number of the close parentheses
            if close_parenthes == 0:
                # check it is valid or not
                if self.isValid(instant_combination):
                    # if it is valid append it to the result_arr
                    result_arr.append(instant_combination)
                # return (the base case)
                return
            # if the number of the open parentheses is greater than 0
            if open_parenthes != 0:
                # call the recursive function with open_parenthes-1
                recursive_helper(open_parenthes-1, close_parenthes, result_arr, instant_combination + '(')
            # call the recursive function with close_parenthes-1
            recursive_helper(open_parenthes, close_parenthes-1, result_arr, instant_combination + ')')
        # call the recursive function with n, n, result_arr and an empty string
        recursive_helper(n, n, result_arr, '')
        # return the result_arr
        return result_arr
