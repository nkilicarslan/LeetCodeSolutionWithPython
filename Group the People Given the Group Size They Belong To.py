from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result_key = []
        id_index_dict = {}
        for index in range(len(groupSizes)):
            if groupSizes[index] not in id_index_dict:
                id_index_dict[groupSizes[index]] = [index]
            else:
                id_index_dict[groupSizes[index]].append(index)

        dict_keys = list(id_index_dict.keys())
        for key in dict_keys:
            result_key.append([])
            for index in id_index_dict[key]:
                if len(result_key[-1]) < key:
                    result_key[-1].append(index)
                else:
                    result_key.append([index])
        return result_key

a = Solution()
a.groupThePeople([3,3,3,3,3,1,3])