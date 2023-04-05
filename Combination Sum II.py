class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(result_list, remain_value, candidates, combinations):
            for i in candidates:
                if i == remain_value:
                    if combinations + [i] not in result_list:
                        result_list.append(combinations + [i])
                elif i < remain_value:
                    index_of_list = candidates.index(i)
                    helper(result_list, remain_value - i, candidates[index_of_list+1:], combinations + [i])

        helper(res, target, candidates, [])
        return res