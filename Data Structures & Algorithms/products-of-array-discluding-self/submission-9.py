class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        forward = [1] * N
        backward = [1] * N
        res = [1] * N

        for i in range(1, N):
            forward[i] = forward[i - 1] * nums[i - 1]
        
        for i in range(N - 2, -1, -1):
            backward[i] = backward[i + 1] * nums[i + 1]
        
        for i in range(N):
            res[i] = forward[i] * backward[i]
        
        return res

    