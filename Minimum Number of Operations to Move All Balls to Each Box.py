class Solution:
    # this function will return the minimum number of operations required to move all the balls to the ith box
    def minOperations(self, boxes: str) -> List[int]:
        # create a list to store the indices of the boxes with 1
        index_of_ones = []
        # create a list to store the result
        result_list = []
        # iterate over the boxes
        for index in range(len(boxes)):
            # if the box has 1, append the index to the index_of_ones list
            if boxes[index] == "1":
                index_of_ones.append(index)
        # iterate over the boxes
        for i in range(len(boxes)):
            # create a variable to store the sum of the absolute difference between the index of the box and the index of the boxes with 1
            sum = 0
            # iterate over the indices of the boxes with 1
            for j in index_of_ones:
                # add the absolute difference between the index of the box and the index of the boxes with 1 to the sum
                sum += abs(j-i)
            # append the sum to the result list
            result_list.append(sum)
        return result_list
