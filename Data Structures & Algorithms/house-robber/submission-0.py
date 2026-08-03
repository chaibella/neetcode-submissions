class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0 # prev-prev, prev
        for n in nums:
            a, b = b, max(b, n + a)
        return b