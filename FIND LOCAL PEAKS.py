class Solution:
    def solve(self, nums):
        if len(nums) == 1:
            return []
        lis = []
        n = len(nums)
        for i in range(n):
            if i == 0 and nums[i] > nums[i + 1]:
                lis.append(i)
            elif i == n - 1 and nums[i] > nums[i - 1]:
                lis.append(i)
            elif nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                lis.append(i)
        return lis
