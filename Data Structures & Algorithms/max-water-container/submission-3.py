class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            res = max(res, cur)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1


        return res
        