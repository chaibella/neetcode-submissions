class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            
            cur = 1
            while num + 1 in nums_set:
                num += 1
                cur += 1

            longest = max(longest, cur)
        
        return longest