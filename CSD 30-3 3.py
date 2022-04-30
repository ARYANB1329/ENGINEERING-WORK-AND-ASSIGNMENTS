# ARYAN SHIV SIDDHABATHULA 121910313029 (B13 29)
# Given a string s, consisting of "X" and "Y"s, delete the minimum number of characters such that there's no
# consecutive "X" and no consecutive "Y".

s = "YYYXYXX"
l = []
for i in s:
    l.append(i)

for i in range(len(l)):
    k = i + 1
    if k == len(l):
        break
    if i == 0:
        if l[i] == l[k]:
            l[i] = 1
    if l[i - 1] == 1:
        if l[i] == l[k]:
            l[i] = 1
    if l[i] != l[i - 1] and l[i] == l[k]:
        l[i + 1] = 1
s = ''
for i in l:
    if i != 1:
        s = s + i
print(s)
