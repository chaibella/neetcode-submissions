class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in pairs:
                return [pairs[pair], i]
            pairs[num] = i
        return [-1, -1]