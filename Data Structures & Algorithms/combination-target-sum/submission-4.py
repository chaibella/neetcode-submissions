class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, path, remains):
            if remains == 0: # added to target, add path to res
                res.append(path[:])
                return
            if i == len(nums):
                return # ran out of numbers or exceeded target

            if nums[i] <= remains: # only use current num if it wont overflow
                path.append(nums[i]) # use current num
                dfs(i, path, remains - nums[i]) # and try
                path.pop() # discard/skip current num
            dfs(i + 1, path, remains) # and try with next num
        
        nums.sort() # sort to stop early
        res = []
        dfs(0, [], target)
        return res