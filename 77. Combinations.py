class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # create a list to store the combinations
        combinations = []
        # create a function to generate the combinations
        def generate_combinations(start, combination):
            # if the length of the combination is equal to k
            if len(combination) == k:
                # append the combination to the combinations list
                combinations.append(combination.copy())
                # return
                return
            # iterate over the range from start to n
            for i in range(start, n+1):
                # call the generate_combinations function with the current i and the combination list
                generate_combinations(i+1, combination + [i])
        # call the generate_combinations function with 1 and an empty list
        generate_combinations(1, [])
        # return the combinations list
        return combinations