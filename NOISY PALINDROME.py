class Solution:
    def solve(self, s):
        ns=''
        for c in s:
            if ord(c) in range(97,123):
                ns=ns+c
        rns=''
        for c in reversed(ns):
            rns=rns+c
        if ns==rns:
            return True
        else:
            return False
