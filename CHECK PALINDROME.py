class Solution:
    def solve(self, s):
        # Write your code here
        rs=''
        for i in reversed(s):
            rs=rs+i
        if s==rs:
            return True
        else:
            return False