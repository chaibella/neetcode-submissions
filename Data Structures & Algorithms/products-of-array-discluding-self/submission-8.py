class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        prefix, postfix = 1, 1

        for i in range(N):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(N-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        