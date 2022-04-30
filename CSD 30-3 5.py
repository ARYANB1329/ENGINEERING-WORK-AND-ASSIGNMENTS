# ARYAN SHIV SIDDHABATHULA 121910313029 (B13 29)
# Given two strings s0 and s1, return whether you can obtain s1 by removing 1 letter from s0.

s0 = input()
s1 = input()
t = []
w1 = []
for i in range(len(s0)):
    c = 0
    while c < len(s0):
        if c != i:
            t.append(s0[c])
        c += 1
        if c == len(s0):
            break
    s = ''
    for j in t:
        s = s + j
    w1.append(s)
    t.clear()
for i in w1:
    if i == s1:
        t = 1
if t == 1:
    print("True")
else:
    print("False")
