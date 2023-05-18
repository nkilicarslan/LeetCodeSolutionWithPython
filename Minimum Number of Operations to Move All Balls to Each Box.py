class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_of_ones = []
        result_list = []
        for index in range(len(boxes)):
            if boxes[index] == "1":
                index_of_ones.append(index)
        for i in range(len(boxes)):
            sum = 0
            for j in index_of_ones:
                sum += abs(j-i)
            result_list.append(sum)
        return result_list
