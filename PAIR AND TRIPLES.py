class Solution:
    def solve(self, s):
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        pair=False
        for k in d:
            if d[k]==2:
                pair=True
                d[k]-=2
                break
            elif (d[k]-2)%3==0:
                pair=True
                d[k]-=2
                break
        if pair==False:
            return False
        for k in d:
            if d[k]%3!=0:
                return False
        return True

