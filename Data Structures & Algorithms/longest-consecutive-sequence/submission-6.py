class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        vals = set(nums)

        for num in nums:
            if num - 1 in vals: # chain already explored
                continue

            cur = 1
            while num + cur in vals:
                cur += 1
            res = max(res, cur)

        return res