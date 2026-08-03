class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(houses):
            prev2, prev1 = 0, 0
            for house in houses:
                prev2, prev1 = prev1, max(prev1, house + prev2)
            return prev1

        exclude_last = helper(nums[:-1])
        exclude_first = helper(nums[1:])
        return max(exclude_first, exclude_last)