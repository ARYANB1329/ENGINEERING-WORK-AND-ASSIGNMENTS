# ARYAN SHIV SIDDHABATHULA 121910313029 (B13 29)
# The string ABC has 6 permutations, i.e., ABC, ACB, BAC, BCA, CBA, CAB. In Python, we can use the built-in module
# itertools to get permutations of elements in the list using the permutations() function. Input : str = 'ABC' Output
# : ABC ACB BAC BCA CAB CBA
from itertools import permutations

input1 = 'ABC'
p = permutations(input1, len(input1))
for i in p:
    print(''.join(i))

