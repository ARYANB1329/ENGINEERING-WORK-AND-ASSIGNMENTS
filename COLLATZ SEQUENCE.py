class Solution:
    def solve(self, n):
        ct=1
        while n!=1:
            if n%2==0:
                n=n//2
                ct+=1
            else:
                n=(n*3)+1
                ct+=1
        return ct