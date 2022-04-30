# ARYAN SIDDHABATHULA 121910313029
# B13 29

from collections import Counter
nums = list(map(int, input().split()))
x=Counter(nums)
s = set()
for i in range(0, len(x)):
  s.add(x[i])
if(len(s) == len(x)):
  print("False")
else:
  print("True")