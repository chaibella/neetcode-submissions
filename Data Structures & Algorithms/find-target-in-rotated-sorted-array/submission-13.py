class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # found target
            if nums[m] == target:
                return m

            # left is sorted, and target in between
            # left is not sorted, and target in between
            # ... target > left or target < right
            if ((nums[l] <= nums[m] and nums[l] <= target <= nums[m]) or
                (nums[l] > nums[m] and (target >= nums[l] or target < nums[m]))):
                r = m - 1
            # otherwise search right
            else:
                l = m + 1

        return -1