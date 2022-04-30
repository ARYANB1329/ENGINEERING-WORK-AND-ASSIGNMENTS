# check if it is a valid CFG rule or not
# checking both LHS and RHS parts
k = input("Enter Input: ")
l, r = k.split('->')
lflag = 0
rflag = 0
if len(l) == 1 and l[0].isupper():
    lflag = 1
for j in r:
    x = r.split("/")
ri = []
for i in x:
    if i != '':
        ri.append(i)
    if len(ri) != 0:
        rflag = 1
    if lflag == 1 and rflag == 1:
        print("Its a Valid CFG rule")
    else:
        print("Its an Invalid CFG rule!")