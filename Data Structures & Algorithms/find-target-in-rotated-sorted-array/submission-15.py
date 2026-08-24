class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # found target
            if nums[m] == target:
                return m

            # continue left if either of these is true
            # NO pivot in left half and target is within range
            # YES pivot in left half and target within wrapped range
            if ((nums[l] <= nums[m] and nums[l] <= target < nums[m]) or 
                (nums[l] > nums[m] and (target >= nums[l] or target < nums[m]))):
                r = m - 1

            # otherwise continue right
            else:
                l = m + 1
        return -1