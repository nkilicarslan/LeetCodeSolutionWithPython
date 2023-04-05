class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # create a var to store the result
        result_arr = []
        # get the length of the string
        length_s = len(s)

        # create a bfs function
        def bfs(start_index, combination):
            # if the start_index is greater than or equal to the length of the string, then append it
            if start_index >= length_s:
                result_arr.append(combination.copy())
                return
            # otherwise iterate over the string
            else:
                for end_index in range(start_index, length_s):
                    # if the substring is a palindrome then append it to the combination and call the bfs function
                    if s[start_index:end_index + 1] == s[start_index:end_index + 1][::-1]:
                        combination.append(s[start_index:end_index + 1])
                        bfs(end_index + 1, combination)
                        combination.pop()
        # call the bfs function
        bfs(0, [])
        return result_arr
