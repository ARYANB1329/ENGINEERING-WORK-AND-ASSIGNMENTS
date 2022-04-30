# ARYAN SIDDHABATHULA 121910313029
# B13 29

s=input()
o = 0
c = 0
for i in s:
    if i == "(":
        o += 1
    else:
        if o == 0:
            c += 1
        else:
            o -= 1
print(o+c)