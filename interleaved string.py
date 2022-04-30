from collections import deque
class Solution:
    def solve(self, s0, s1):
        # Write your code here
        d0,d1=deque(s0),deque(s1)
        s=''
        lis=list(zip(s0,s1))
        for i in lis:
            d0.popleft()
            d1.popleft()
        for x,y in lis:
           s=s+x+y
        if len(list(d0))!=0:
            for c in d0:
                s=s+c
        if len(list(d1))!=0:
            for c in d1:
                s=s+c
        return s