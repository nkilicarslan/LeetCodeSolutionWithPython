class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time_metal = 0
        time_paper = 0
        time_glass = 0
        total_time = 0
        for i in range(len(garbage)):
            for char in garbage[i]:
                if char == "G":
                    total_time += (time_glass + 1)
                    time_glass = 0
                elif char == "M":
                    total_time += (time_metal + 1)
                    time_metal = 0
                else:
                    total_time += (time_paper + 1)
                    time_paper = 0
            if i == len(garbage) - 1:
                break
            time_glass += travel[i]
            time_paper += travel[i]
            time_metal += travel[i]
        return total_time
