class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # find intersecting point first
        # find the min_left_value of the intersecting rectangle
        min_left_value = max(ax1, bx1)
        # find the min_right_value of the intersecting rectangle
        min_right_value = min(ax2, bx2)
        # find the min_top_value of the intersecting rectangle
        min_top_value = min(ay2, by2)
        # find the min_bottom_value of the intersecting rectangle
        min_bottom_value = max(ay1, by1)
        # calculate the total area of the first rectangle
        first_rect_area = (ax2 - ax1) * (ay2 - ay1)
        # calculate the total area of the second rectangle
        second_rect_area = (bx2 - bx1) * (by2 - by1)
        # check there is an intersecting rectangle or not if not return the sum of the first_rect_area and second_rect_area
        if (min_right_value - min_left_value) < 0 or (min_top_value- min_bottom_value) < 0:
            return first_rect_area + second_rect_area
        # else if there is an intersecting rectangle
        # calculate the total area of the intersecting rectangle
        intersecting_total_area = (min_right_value - min_left_value) * (min_top_value- min_bottom_value)
        # return the sum of the first_rect_area, second_rect_area then subtract the intersecting_total_area
        return first_rect_area + second_rect_area - intersecting_total_area
