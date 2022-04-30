class Solution:
    def solve(self, s):
        # Write your code here
        lis=[]
        for i in range(len(s)):
            if s[i] not in lis:
                lis.append(s[i])
            else:
                return i
        return -1