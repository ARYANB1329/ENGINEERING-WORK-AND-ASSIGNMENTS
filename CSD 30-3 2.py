# ARYAN SHIV SIDDHABATHULA 121910313029 (B13 29)
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any
# order.Input: nums = [1,2,3] Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from itertools import permutations

input1 = list(map(int, input().split()))
p = permutations(input1, len(input1))
for i in p:
    print(list(i))
