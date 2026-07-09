class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: # rotation on right side and
                l = m + 1         # mid num > so toss mid and left
            else:
                r = m
        
        return nums[r]