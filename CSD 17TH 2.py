# Given two strings 's1' and 's2' return the two strings interleaved, starting with s1. If there are leftover
# characters in a string they should be added to the end.

s1 = input("Enter string: ")
s2 = input("Enter string: ")

n = min(len(s1), len(s2))
res = ''
for i in range(n):
    res += s1[i] + s2[i]
if n < len(s1):
    res += s1[n:]
else:
    res += s2[n:]
print(res)

# Name: Aryan Shiv Siddhabathula
