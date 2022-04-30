class Solution:
    def solve(self, nums):
        nums.sort()
        mx1=nums[-1]*nums[-2]*nums[-3]
        mx2=nums[0]*nums[1]*nums[-1]
        return max(mx1,mx2)