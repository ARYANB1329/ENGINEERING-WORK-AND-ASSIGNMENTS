# No of Terminals in RHS (a-z) (special symbols)
k = input("Enter CFG: ")
l, r = k.split('->')
x = r.split("/")
arr = []
for i in x:
    if i != '':
        arr.append(i)
count = 0
for i in range(len(arr)):
    a = arr[i]
    for j in range(len(a)):
        if not a[j].isupper():
            count = count + 1
print("No of Terminals", count)
