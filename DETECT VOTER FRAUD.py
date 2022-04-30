from collections import Counter
class Solution:
    def solve(self, votes):
        lis=[]
        for i,j in votes:
            lis.append(j)
        ct=Counter(lis)
        nlis=list(ct.items())
        for i,j in nlis:
            if j>1:
                return True
        return False