class Solution:
    # this function will return the minimum amount of time to collect the garbage
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # create variables to store the time taken to collect the garbage of each type and the total time
        time_metal = 0
        time_paper = 0
        time_glass = 0
        total_time = 0
        # iterate over the garbage
        for i in range(len(garbage)):
            # iterate over the garbage of each type
            for char in garbage[i]:
                # if the garbage is of type "G", add the time taken to collect the garbage of type "G" to the total time and reset the time taken to collect the garbage of type "G"
                if char == "G":
                    total_time += (time_glass + 1)
                    time_glass = 0
                # if the garbage is of type "M", add the time taken to collect the garbage of type "M" to the total time and reset the time taken to collect the garbage of type "M"
                elif char == "M":
                    total_time += (time_metal + 1)
                    time_metal = 0
                # if the garbage is of type "P", add the time taken to collect the garbage of type "P" to the total time and reset the time taken to collect the garbage of type "P"
                else:
                    total_time += (time_paper + 1)
                    time_paper = 0
            # if the garbage is the last garbage, break the loop in order to prevent index out of range error
            if i == len(garbage) - 1:
                break
            # add the time taken to travel to the next garbage to the total time and the time taken to collect the garbage of each type
            time_glass += travel[i]
            time_paper += travel[i]
            time_metal += travel[i]
        # return the total time
        return total_time
