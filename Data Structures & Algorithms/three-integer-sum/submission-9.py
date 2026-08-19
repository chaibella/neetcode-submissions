class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)

        for i in range(0, N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, N - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur < 0:
                    l += 1
                elif cur > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1

        return res
