class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                # we could check which pillar height is larger between left pointer or right pointer, but it really does
                # not matter.
                r -= 1
        return res