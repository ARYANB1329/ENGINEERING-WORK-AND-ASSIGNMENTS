class Solution:
    def solve(self, lst0, lst1):
        # Write your code here
        lst0.extend(lst1)
        lst0.sort()
        return lst0

