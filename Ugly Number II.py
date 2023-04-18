class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # create a list to store the ugly numbers
        result_list = [1]
        # create three pointers to store the positions of the ugly numbers
        p1 = 0
        p2 = 0
        p3 = 0
        # iterate until the length of the result_list is equal to n
        while len(result_list) != n:
            # calculate the minimum of the ugly numbers
            min_result = min(result_list[p3] * 5, min(result_list[p1] * 2, result_list[p2] * 3))
            # append the minimum to the result_list
            result_list.append(min_result)
            # update the pointers
            if result_list[p1] * 2 == min_result:
                p1 += 1
            if result_list[p2] * 3 == min_result:
                p2 += 1
            if result_list[p3] * 5 == min_result:
                p3 += 1
        # return the last element of the result_list
        return result_list[-1]
