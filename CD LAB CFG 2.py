# check if CFG - RHS part satisfies.
# rules for RHS:
# length = any length (no restriction)
# type = anything --> (0-9, A-Z, a-Z, operators(+,-,/,*,%),..)
k = input("Enter input: ").split('->')
x = k[1].split("/")
r = []
for i in x:
    if i != '':
        r.append(i)
if len(r) != 0:
    print("It satisfies the RHS rules of CFG")
else:
    print("Not a valid RHS of CFG!")
