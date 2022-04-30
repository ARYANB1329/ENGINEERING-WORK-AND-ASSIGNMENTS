class Solution:
    def solve(self, nums):
        nums.sort()
        mx = 0
        for i in range(1, len(nums)):
            curr = nums[i] - nums[i - 1]
            mx = max(mx, curr)
        return mx
