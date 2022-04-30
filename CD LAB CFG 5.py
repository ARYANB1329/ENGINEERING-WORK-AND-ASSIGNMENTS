# take a CFG as input
# display its RHS part
k = input("Enter CFG: ")
l, r = k.split('->')
x = r.split("/")
arr = []
for i in x:
    if i != '':
        arr.append(i)
print("RHS part of the given CFG is: ", arr)
