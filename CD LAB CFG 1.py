# check if CFG - LHS part satisfies or not
# rules for LHS:
# length = 1
# type = NT --> (A-Z)
l = input("Enter input: ")
k = l.split('->')
if len(k[0]) == 1 and k[0].isupper():
    print("It satisfies the LHS rules of CFG")
else:
    print("Not a valid LHS of CFG!")
