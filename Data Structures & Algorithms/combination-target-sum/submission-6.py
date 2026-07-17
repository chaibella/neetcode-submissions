class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # sorted to stop early once number gets too big
        res = [] 

        def dfs(i, path, remains):
            if remains == 0: # found match, add copy of path
                res.append(path[:])
                return
            if i == len(nums) or nums[i] > remains:
                return # ran out of numbers, or number is too big (sorted)
            
            path.append(nums[i])
            dfs(i, path, remains - nums[i]) # reuse current number
            path.pop()
            dfs(i + 1, path, remains) # skip current number

        dfs(0, [], target)
        return res