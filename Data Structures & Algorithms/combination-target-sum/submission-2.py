class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def dfs(i=0, vals=[], cur=0):
            if i >= len(nums):
                return # used up all nums, no more to incorporate
            if cur == target: # already satisfies target, add to result
                res.append(vals[:])
                return
            
            vals.append(nums[i])
            cur += nums[i]
            if cur <= target:
                dfs(i, vals, cur)
            vals.pop()
            cur -= nums[i]
            dfs(i + 1, vals, cur)
        
        res = []
        dfs()
        return res