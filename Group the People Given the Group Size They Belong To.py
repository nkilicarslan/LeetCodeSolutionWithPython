from typing import List
class Solution:
    # this function will return the groups of people with the given group sizes
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # create a result array
        result_key = []
        # create a dictionary to store the group sizes and the indices of the people
        id_index_dict = {}
        # iterate over the group sizes
        for index in range(len(groupSizes)):
            # if the group size is not in the dictionary, add the group size and the index to the dictionary
            if groupSizes[index] not in id_index_dict:
                id_index_dict[groupSizes[index]] = [index]
            # otherwise append the index to the list of indices
            else:
                id_index_dict[groupSizes[index]].append(index)
        # get the keys of the dictionary
        dict_keys = list(id_index_dict.keys())
        # iterate over the keys
        for key in dict_keys:
            # append the empty list to the result array
            result_key.append([])
            # iterate over the indices of the key
            for index in id_index_dict[key]:
                # if the length of the last list in the result array is less than the key, append the index to the last list
                if len(result_key[-1]) < key:
                    result_key[-1].append(index)
                # otherwise append the empty list to the result array and append the index to the last list
                else:
                    result_key.append([index])
        # return the resulted key list
        return result_key
