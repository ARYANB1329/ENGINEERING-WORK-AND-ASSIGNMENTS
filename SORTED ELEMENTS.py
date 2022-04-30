class Solution:
    def solve(self, nums):
        lis = nums.copy()
        nums.sort()
        ct = 0
        for i in range(len(nums)):
            if nums[i] == lis[i]:
                ct += 1
        return ct
