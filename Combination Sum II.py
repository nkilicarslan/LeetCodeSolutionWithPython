class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # create a res to store the result and sort the candidates
        res = []
        candidates.sort()
        # create a helper function to recursively find the combinations
        def helper(position, remain_value, combinations):
            # if the remaning value is 0 append the combinations to the res and return
            if remain_value == 0:
                res.append(combinations.copy())
                return
            #if the remaining value is less than 0 return
            if remain_value < 0:
                return

            prev_value = -1
            # iterate over the candidates list
            for i in range(position, len(candidates)):
                # if the prev_value is equal to the current value then continue
                if prev_value == candidates[i]:
                    continue
                # otherwise append the current value to the combinations and call the helper function
                else:
                    combinations.append(candidates[i])
                    helper(i+1, remain_value - candidates[i], combinations)
                    combinations.pop()
                    prev_value = candidates[i]
        # call the helper function
        helper(0, target, [])
        return res
